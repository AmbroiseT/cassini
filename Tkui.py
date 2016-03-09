from tkinter import *
from reader import createMapFromFile
from palette import paletteStandard

from Echelle import Echelle


mapData = createMapFromFile("data/map2.osm")

mapData.describe()
echelle = Echelle(mapData, maxX=500)
echelle.describe()
print("Une longitude de 2.221 donne {} pixels".format(echelle.convertLonPosToPx(2.221)))
print("Une latitude de 48.8514 donne {} pixels".format(echelle.convertLatPosToPx(48.8514)))

top = Tk()

canvas = Canvas(top, width=echelle.maxX, height=echelle.maxY)


palette = paletteStandard()
maxlen = 0
minlen = 1000
print("Nombre de ways : {}".format(len(mapData.ways)))
for key, way in mapData.ways.items():
	points = [( echelle.convertLonPosToPx(node.lon), echelle.convertLatPosToPx(node.lat)) for node in way.nodes]
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
	if(len(points)<50 and len(points)>2 and way.isArea()):
		canvas.create_polygon(points, fill=color, width=3)

print("Maxlen = {}".format(maxlen))
print("Minlen = {}".format(minlen))
canvas.pack()


top.mainloop()
