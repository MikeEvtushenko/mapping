import folium
import pandas

# Создаем объект pandas для загрузки таблицы
data = pandas.read_csv("Volcanoes.txt")
# Вытаскиваем в список две колонки (широта, долгота), список колонок - data.columns
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
# tiles - стиль ландшафта. Список есть есть в help(folium.Map)
map_1 = folium.Map(location=[42.924869, -108.755439], zoom_start=5, tiles="Stamen Terrain")

# fg = feature group - отдельный объект, содержащий слои, точки и т.д.
fg = folium.FeatureGroup(name="My Map")

for latitude, longitude, elevation, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, elevation), width=200, height=100)
    fg.add_child(
        folium.Marker(location=[latitude, longitude], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))
map_1.add_child(fg)
map_1.save("Map1.html")
