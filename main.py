from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query=city
        results = geocoder.geocode(query)
        if results:
            lat=round(results[0]["geometry"]["lat"],3)
            lng=round(results[0]["geometry"]["lng"],3)

            return f"Широта:{lat}, Долгота:{lng}"
        else:
            return "Данные не найдены"
    except Exception as err:
        print(f"Неизвестная ошибка {err}")

key = 'aea38c6f1db14c1da396e3ab10e1f936'
city="Moscow"
coordinates=get_coords(city, key)


print(f"Координаты города {city}: {coordinates}")