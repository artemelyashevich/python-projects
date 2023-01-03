import turtle
from random import choice, randint
import time

delay = 0.1
score_a = 0
score_b = 0

window = turtle.Screen()
window.setup(1100, 600)
window.title("Ping Pong")
window.tracer()

border = turtle.Turtle()
border.pensize(3)
border.speed(0)
border.hideturtle()
border.up()
border.goto(-500, 250)
border.down()
border.goto(500, 250)
border.goto(500, -250)
border.goto(-500, -250)
border.goto(-500, 250)

rocket_a = turtle.Turtle()
rocket_a.up()
rocket_a.color("grey20")
rocket_a.speed(0)
rocket_a.goto(-490, 0)
rocket_a.shape("square")
rocket_a.shapesize(5, 1)

rocket_b = turtle.Turtle()
rocket_b.up()
rocket_b.color("grey20")
rocket_b.speed(0)
rocket_b.goto(490, 0)
rocket_b.shape("square")
rocket_b.shapesize(5, 1)

center_line = turtle.Turtle()
center_line.speed(0)
center_line.hideturtle()
center_line.up()
center_line.pensize(3)
center_line.goto(0, 250)
center_line.right(90)
uc = 0
for i in range(21):
    if i != 20:
        if uc % 2 == 0:
            center_line.down()
            center_line.forward(24)
        else:
            center_line.up()
            center_line.forward(24)
        uc += 1
    elif i == 20:
        center_line.down()
        center_line.forward(20)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.dx = 3
ball.dy = 3
ball.up()


def left_up():
    if rocket_a.ycor() >= 200:
        rocket_a.sety(190)
    y = rocket_a.ycor() + 10
    rocket_a.sety(y)


def left_down():
    if rocket_a.ycor() <= -200:
        rocket_a.sety(-190)
    y = rocket_a.ycor()
    rocket_a.sety(y - 10)


def right_up():
    if rocket_b.ycor() >= 200:
        rocket_b.sety(190)
    y = rocket_b.ycor() + 10
    rocket_b.sety(y)


def right_down():
    if rocket_b.ycor() <= -200:
        rocket_b.sety(-190)
    y = rocket_b.ycor()
    rocket_b.sety(y - 10)


window.listen()
window.onkeypress(left_up, "w")
window.onkeypress(left_down, 's')
window.onkeypress(right_up, "Up")
window.onkeypress(right_down, 'Down')

FONT = 'Tahoma', 35

label_a = turtle.Turtle()
label_a.penup()
label_a.speed(0)
label_a.hideturtle()
label_a.goto(-500, 250)
label_a.write(score_a, font=FONT)

label_b = turtle.Turtle()
label_b.penup()
label_b.speed(0)
label_b.hideturtle()
label_b.goto(480, 250)
label_b.write(score_b, font=FONT)
ball.dx = choice([-1, -2, -3, 1, 2, 3])
ball.dy = choice([-1, -2, -3, 1, 2, 3])

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 240:
        ball.dy = -ball.dy
    if ball.ycor() <= -240:
        ball.dy = -ball.dy
    if ball.xcor() <= -490:
        score_b += 1
        label_b.clear()
        label_b.write(score_b, font=FONT)
        time.sleep(delay)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-1, -2, -3, 1, 2, 3])

    if ball.xcor() >= 490:
        score_a += 1
        label_a.clear()
        label_a.write(score_a, font=FONT)
        time.sleep(delay)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-1, -2, -3, 1, 2, 3])

    if ball.distance(rocket_b) < 25:
        ball.dx = -ball.dx
    if ball.distance(rocket_a) < 25:
        ball.dx = -ball.dx

# window.mainloop()
