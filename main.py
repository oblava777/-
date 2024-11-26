from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat=round(results[0]["geometry"]["lat"],3)
            lng=round(results[0]["geometry"]["lng"],3)
            country = results[0]['components']['country']
            region = results[0]['components']['state']

            return f"Широта:{lat}, Долгота:{lng} Страна: {country} Регион: {region}"
        else:
            return "Данные не найдены"
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {coordinates}")



key = 'aea38c6f1db14c1da396e3ab10e1f936'



win = Tk()
win.title('Координаты городов')
win.geometry('300x100')

entry = Entry()
entry.pack()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

win.mainloop()