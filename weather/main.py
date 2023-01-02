from config import key
import requests
from tkinter import Tk, StringVar, Label, Entry, Button

root = Tk()
root.title("Weather")
root.geometry("500x400")
root.resizable(width=False, height=False)

city_value = StringVar()

label1 = Label(text="Enter city:", font=40)
city = Entry(textvariable=city_value, font=40)
btn = Button(text="Search", font=40)

temp = Label(text="", font=35)
max_temp = Label(text="", font=35)
min_temp = Label(text="", font=35)
humidity = Label(text="", font=35)
pressure = Label(text="", font=35)
error = Label(text="Error", font=50)
title = Label(text="Weather", font=45)


def test(event):
    try:
        city_v = city_value.get()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_v}&appid={key}'
        r = requests.get(url)
        data = r.json()

        temp['text'] = data["main"]["temp"]
        max_temp['text'] = f'Максимальная температура: {int(data["main"]["temp_max"] - 273)}C'
        min_temp['text'] = f'Минимальная температура: {int(data["main"]["temp_min"] - 273)}C'
        humidity['text'] = f'Влажность: {data["main"]["humidity"]}%'
        pressure['text'] = f'Давление: {data["main"]["pressure"]}'

        temp.grid(row=1, column=2)
        max_temp.grid(row=5, column=2)
        min_temp.grid(row=6, column=2)
        humidity.grid(row=7, column=2)
        pressure.grid(row=8, column=2)

    except Exception as e:
        error.grid(row=5, column=2)


title.grid(row=1, column=1)
label1.grid(row=2, column=2)
city.grid(row=3, column=2)
btn.grid(row=4, column=2)

if __name__ == "__main__":
    btn.bind('<Button-1>', test)
    root.mainloop()
