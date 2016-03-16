import math
from structure import ParsedMap


class Echelle:
    map = None
    # Facteur multiplicatif pour faire une projection des coords
    mult = 40000 / 360
    # Facteur correctif pour la longitude(a calculer en fonction de la latitude)
    corr = 1

    maxX = 500
    maxY = 500

    #Attributes for zooming and moving :
    zoom = 1
    #Relative position in km
    corner = (0, 0)

    factor_km_px = 1

    width_km = 0
    height_km = 0

    def __init__(self, map, maxX=500):
        assert isinstance(map, ParsedMap)
        self.maxX = maxX
        self.map = map
        self.corr = math.cos(math.radians(self.map.max_lat))
        self.height_km = self.convert_lat_to_km(self.map.max_lat - self.map.min_lat)
        self.width_km = self.convert_lon_to_km(self.map.max_lon - self.map.min_lon)
        self.factor_km_px = self.maxX / self.width_km
        self.maxY = self.convert_km_to_px(self.height_km)
        self.zoom = 1
        self.corner = (0, 0)

    def convert_lat_to_km(self, latitude):
        return latitude * self.mult

    def convert_lon_to_km(self, longitude):
        return longitude * self.mult * self.corr

    def convert_lat_to_px(self, latitude):
        return self.convert_km_to_px(self.convert_lat_to_km(latitude)) * self.zoom

    def convert_lon_to_px(self, longitude):
        return self.convert_km_to_px(self.convert_lon_to_km(longitude)) * self.zoom

    def convert_lat_pos_to_px(self, lat):
        return self.maxY - self.convert_km_to_px_y(self.convert_lat_to_km(lat - self.map.min_lat))

    def convert_lon_pos_to_px(self, lon):
        return self.convert_km_to_px_x(self.convert_lon_to_km(lon - self.map.min_lon))

    def convert_km_to_px(self, km):
        return self.factor_km_px * km * self.zoom

    def convert_km_to_px_x(self, km):
        return (self.factor_km_px + self.corner[0]) * km * self.zoom

    def convert_km_to_px_y(self, km):
        return (self.factor_km_px + self.corner[1]) * km * self.zoom

    def describe(self):
        print("Echelle de la carte")
        print("Facteur multiplicatif = {}".format(self.mult))
        print("Facteur correctif = {}".format(self.corr))
        print("Un degré de longitude fait {} km".format(self.corr * self.mult))
        print("Latitude max {}".format(self.map.max_lat))
        print("Largeur Km = {}, hauteur Km = {}".format(self.width_km, self.height_km))
        print("MaxX = {}, maxY={}".format(self.maxX, self.maxY))
        print("Facteur Km to Px : {}".format(self.factor_km_px))
