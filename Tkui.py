from tkinter import *
from reader import create_map_from_file
from magic import createMagicMap
from palette import paletteStandard

from Echelle import Echelle


mapData = create_map_from_file("data/map3.osm")

mapData.describe()
echelle = Echelle(mapData, maxX=500)
echelle.describe()
print("Une longitude de 2.221 donne {} pixels".format(echelle.convert_lon_pos_to_px(2.221)))
print("Une latitude de 48.8514 donne {} pixels".format(echelle.convert_lat_pos_to_px(48.8514)))

magic = createMagicMap()

top = Tk()

canvas = Canvas(top, width=echelle.maxX, height=echelle.maxY)


palette = paletteStandard()
maxlen = 0
minlen = 1000
print("Nombre de ways : {}".format(len(mapData.ways)))
for key, way in mapData.ways.items():
	points = [(echelle.convert_lon_pos_to_px(node.lon), echelle.convert_lat_pos_to_px(node.lat)) for node in way.nodes]
	#print("Way {} has {} nodes".format(way.id, len(way.nodes)))
	maxlen = len(points) if len(points)>maxlen else maxlen
	minlen = len(points) if len(points)<minlen else minlen
	color = 'black'
	if('highway' in way.tags):
		color = palette.get('highway')
	if("building" in way.tags):
		color = palette.get("building")
	if("waterway" in way.tags):
		color = palette.get("waterway")
	if('landuse' in way.tags or ('leisure' in way.tags and way.tags['leisure']=='pitch')):
		color = palette.get("landuse")
		print("Landuse element = {}".format(way))
	if len(points)<50 and len(points)>2 and way.isArea():
		canvas.create_polygon(points, fill=color, outline='black', width=1)
	elif magic.get(way.tags.get("highway")) != None:
		dimension = echelle.convert_km_to_px(magic.get(way.tags["highway"]))
		for i in range(len(points)-1):
			canvas.create_line(points[i], points[i+1], fill="black", width=dimension)
print("Maxlen = {}".format(maxlen))
print("Minlen = {}".format(minlen))
canvas.pack()


top.mainloop()
