import folium

# tiles - стиль ландшафта. Список есть есть в help(folium.Map)
map_1 = folium.Map(location=[55.826281, 37.637587], zoom_start=10, tiles="Stamen Terrain")

# fg = feature group - отдельный объект, содержащий слои, точки и т.д.
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[55.81, 37.61], [55.85, 37.65]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Я есть значок", icon=folium.Icon(color="green")))

map_1.add_child(fg)

map_1.save("Map1.html")
