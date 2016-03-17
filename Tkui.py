from tkinter import *
from reader import create_map_from_file
from palette import Style

from Echelle import Echelle


class TkUI():

    def __init__(self, mapdata, echelle, style):
        self.mapdata = mapdata
        self.echelle = echelle
        self.style = style
        self.top = Tk()
        self.canvas = Canvas(self.top, width=self.echelle.maxX, height=self.echelle.maxY)
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind_all("<Key>", self.on_key_pressed)

        self.draw()

        self.canvas.pack()
        self.top.mainloop()

    def draw(self):
        self.canvas.delete("all")
        for way in self.mapdata.ways.values():
            points = [(self.echelle.convert_lon_pos_to_px(node.lon), self.echelle.convert_lat_pos_to_px(node.lat)) for node in way.nodes]

            style_parameters = self.style.get_parameters(way)
            if 2 < len(points) < 50 and way.isArea() and style_parameters.get("visible", False):
                self.canvas.create_polygon(points, fill=style_parameters.get('color', 'black'),
                                           outline=style_parameters.get('line-color', 'black'),
                                           width=0.2 * self.echelle.convert_km_to_px(style_parameters.get('width', 0)))
            else:
                for i in range(len(points) - 1):
                    self.canvas.create_line(points[i], points[i + 1], fill=style_parameters.get('line-color', 'grey'),
                                            width=self.echelle.convert_km_to_px(style_parameters.get('width', 0)))

    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.echelle.zoom *=1.5
        else:
            self.echelle.zoom /=1.5
        self.draw()
        self.canvas.pack()

    def on_key_pressed(self, event):
        decal = 20
        if event.keysym == "Down":
            self.echelle.corner = (self.echelle.corner[0], self.echelle.corner[1] + self.echelle.convert_px_to_km(decal))
            self.draw()
            self.canvas.pack()
        elif event.keysym == 'Up':
            self.echelle.corner = (self.echelle.corner[0], self.echelle.corner[1] - self.echelle.convert_px_to_km(decal))
            self.draw()
            self.canvas.pack()
        elif event.keysym == 'Right':
            self.echelle.corner = (self.echelle.corner[0] - self.echelle.convert_px_to_km(decal), self.echelle.corner[1])
            self.draw()
            self.canvas.pack()
        elif event.keysym == 'Left':
            self.echelle.corner = (self.echelle.corner[0] + self.echelle.convert_px_to_km(decal), self.echelle.corner[1])
            self.draw()
            self.canvas.pack()


if __name__ == '__main__':
    mapData = create_map_from_file("data/map.osm")

    mapData.describe()
    echelle = Echelle(mapData, maxX=500)
    echelle.describe()

    style = Style()
    interface = TkUI(mapData, echelle, style)