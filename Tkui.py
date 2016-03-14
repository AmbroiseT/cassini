from tkinter import *
from reader import create_map_from_file
from palette import Style

from Echelle import Echelle

mapData = create_map_from_file("data/map3.osm")

mapData.describe()
echelle = Echelle(mapData, maxX=500)
echelle.describe()

top = Tk()

canvas = Canvas(top, width=echelle.maxX, height=echelle.maxY)

style = Style()

for way in mapData.ways.values():
    points = [(echelle.convert_lon_pos_to_px(node.lon), echelle.convert_lat_pos_to_px(node.lat)) for node in way.nodes]

    style_parameters = style.get_parameters(way)
    if 2 < len(points) < 50 and way.isArea() and style_parameters.get("visible", False):
        canvas.create_polygon(points, fill=style_parameters.get('color', 'black'),
                              outline=style_parameters.get('line-color', 'black'),
                              width=0.2 * echelle.convert_km_to_px(style_parameters.get('width', 0)))
    else:
        for i in range(len(points) - 1):
            canvas.create_line(points[i], points[i + 1], fill=style_parameters.get('line-color', 'grey'),
                               width=echelle.convert_km_to_px(style_parameters.get('width', 0)))


canvas.pack()

top.mainloop()
