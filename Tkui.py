from tkinter import *
from reader import createMapFromFile

from Echelle import Echelle

mapData = createMapFromFile("data/map2.osm")

mapData.describe()
echelle = Echelle(mapData, 1000)
echelle.describe()
print("Une longitude de 2.221 donne {} pixels".format(echelle.convertLonPosToPx(2.221)))
print("Une latitude de 48.8514 donne {} pixels".format(echelle.convertLatPosToPx(48.8514)))

top = Tk()

canvas = Canvas(top, width=echelle.maxX, height=echelle.maxY)

canvas.create_polygon([(0, 0), (100, 120), (200, 300)])

maxlen = 0
minlen = 1000
print("Nombre de ways : {}".format(len(mapData.ways)))
for key, way in mapData.ways.items():
	points = [(echelle.convertLatPosToPx(node.lat), echelle.convertLonPosToPx(node.lon)) for node in way.nodes]
	#print("Way {} has {} nodes".format(way.id, len(way.nodes)))
	maxlen = len(points) if len(points)>maxlen else maxlen
	minlen = len(points) if len(points)<minlen else minlen
	if(len(points)<20 and len(points)>2):
		canvas.create_polygon(points)

print("Maxlen = {}".format(maxlen))
print("Minlen = {}".format(minlen))
canvas.pack()


top.mainloop()
