import folium
import pandas


def color_picker(elevation):
    if (elevation <= 1000):
        return "orange"
    elif 1000 <= elevation < 3000:
        return 'blue'
    else:
        return 'red'


data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])  # Loads the data from the csv file (panda lib)
lon = list(data["LON"])
ele = list(data["ELEV"])

# Loads the map   (folium lib)
map1 = folium.Map(location=[lat[0], lon[0]], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")  # Feature group for creating child

for lt, ln, el in zip(lat, lon, ele):  # marker adder
    colorr = color_picker(el)
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln], radius=10, color='grey', fill_color=color_picker(el), fill=True, fill_opacity=0.7,
        popup="%s m" % (el), icon=folium.Icon(color=colorr, icon='hashtag', prefix='fa')))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                       else 'red'}))     # Data from the world json and use the style function

map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())  # Looks for childs
map1.save("map1.html")
