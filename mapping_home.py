import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")         #list of values of volcanoes
lat = list(data["LAT"])     #to fetch the value of latitude alone to a list
lon = list(data["LON"])     #to fetch the value of longitude alone to a list
elev = list(data["ELEV"])   #to fetch the value of elevation alone to a list

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 2000:
        return 'orange'
    else:
        return 'red'
#Base Map
map = folium.Map(location=[-38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
print(map)

fgv= folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ "m",
                                     fill_color=color_producer(el), color='grey', fill_opacity=0.7))

## To add polygon areas via folium, GeoJson is used and added to the feature group
fgp= folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000
                                                      else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")


