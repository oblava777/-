from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat=round(results[0]["geometry"]["lat"],3)
            lng=round(results[0]["geometry"]["lng"],3)

            return f"Широта:{lat}, Долгота:{lng}"
        else:
            return "Данные не найдены"
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}: {coordinates}")



key = 'aea38c6f1db14c1da396e3ab10e1f936'



win = Tk()
win.title('Координаты городов')
win.geometry('200x100')

entry = Entry()
entry.pack()

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

win.mainloop()