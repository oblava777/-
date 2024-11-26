from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat=round(results[0]["geometry"]["lat"],2)
            lng=round(results[0]["geometry"]["lng"],2)
            country = results[0]['components']['country']
            osm_url = f'https://www.openstreetmap.org/?mlat={lat}&mlon={lng}'
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    'coordinates': f"Широта:{lat}, Долгота:{lng}\n Страна: {country}. Регион: {region}",
                    'map_url': osm_url
                }
            else:
                return {
                    'coordinates': f"Широта:{lat}, Долгота:{lng}\n Страна: {country}.",
                    'map_url': osm_url
                }
        else:
            return "Данные не найдены"
    except Exception as err:
        print(f"Неизвестная ошибка {err}")


def show_coordinates(_=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {result['coordinates']}")
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)


key = 'aea38c6f1db14c1da396e3ab10e1f936'
map_url = ''


win = Tk()
win.title('Координаты городов')
win.geometry('300x100')

entry = Entry()
entry.pack()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

map_button = Button(text='Показать карту', command=show_map)
map_button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

win.mainloop()