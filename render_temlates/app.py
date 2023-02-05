import json
from flask import Flask, render_template, request, redirect, jsonify, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
CORS(app)

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=date.today())

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"


class Phone():
    id = int()
    title = str()
    price = int()

    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.id} - {self.title}'


class Article():
    id = int()
    title = str()
    content = str()

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self):
        return f'{self.id} - {self.title}'


@app.route('/phones', methods=["POST", "GET"])
def phones():
    phone1 = Phone(id=1, title="iPhone 9", price=500)
    phone2 = Phone(id=2, title="iPhone 10", price=600)
    phone3 = Phone(id=3, title="iPhone 11", price=700)
    phones = []

    phones.append(phone1)
    phones.append(phone2)
    phones.append(phone3)

    return Response(response=json.dumps([phone.__dict__ for phone in phones]),
                    status=201,
                    mimetype="application/json")


@app.route('/articles', methods=["POST", "GET"])
def articles():
    article1 = Article(id=1, title="Article 1",
                       content='The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.')
    article2 = Article(id=2, title="Article 2",
                       content="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
    article3 = Article(id=3, title="Article 3",
                       content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    articles = []

    articles.append(article1)
    articles.append(article2)
    articles.append(article3)



    return Response(response=json.dumps([article.__dict__ for article in articles]),
                    status=200,
                    mimetype="application/json")


@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


list = Users.query.all()

print(list)


@app.route('/registration', methods=["POST", "GET"])
def blog():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']

        for user in list:
            if user.email == email:
                return render_template("registration.html", error="Пользователь с таким email уже существует")
            elif user.name == name:
                return render_template("registration.html", error="Пользователь с таким именем уже существует")

        try:
            u = Users(email=request.form['email'], psw=request.form['psw'], date=datetime.utcnow())
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                         city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
            print("Post already get ")

            return render_template("data.html")
        except Exception as e:
            print(e)
    return render_template("registration.html")


@app.route('/enter', methods=["POST", "GET"])
def enter():
    if request.method == "POST":

        try:
            email = request.form['email']
            psw = request.form['psw']

            for user in list:
                if user.email == email:
                    # print(psw)
                    if user.psw == psw:
                        user_id = user.id
                        app.logger.info("User founded!" + str(user_id))
                        return redirect('/id/' + str(user_id))
                    else:
                        app.logger.info("invalid password")
                        return render_template("enter.html", err='Invalid password')

            return render_template("enter.html", err='User is not found')

        except Exception as ex:
            app.logger.error(ex)
    return render_template("enter.html")


User = Users.query.all()
Profile = Profiles.query.all()


@app.route(f'/id/<int:user_id>')
def about(user_id):
    user = User[user_id - 1]
    profile = Profile[user_id - 1]
    return render_template("id.html", name=profile.name, old=str(profile.old),
                           city=profile.city, email=user.email)


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
