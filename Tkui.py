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
for key, way in mapData.ways.items():
	points = [(echelle.convertLatPosToPx(node.lat), echelle.convertLonPosToPx(node.lon)) for node in way.nodes]
	#print(points)
	maxlen = len(points) if len(points)>maxlen else maxlen
	canvas.create_polygon(points)

print("Maxlen = {}".format(maxlen))
canvas.pack()


top.mainloop()
