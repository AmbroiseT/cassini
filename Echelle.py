import math


class Echelle:
    map = None
    # Facteur multiplicatif pour faire une projection des coords
    mult = 40000 / 360
    # Facteur correctif pour la longitude(a calculer en fonction de la latitude)
    corr = 1

    maxX = 500
    maxY = 500

    factor_km_px = 1

    width_km = 0
    height_km = 0

    def __init__(self, map, maxX=500):
        self.maxX = maxX
        self.map = map
        self.corr = math.cos(math.radians(self.map.maxlat))
        self.height_km = self.convert_lat_to_km(self.map.maxlat - self.map.minlat)
        self.width_km = self.convert_lon_to_km(self.map.maxlon - self.map.minlon)
        self.factor_km_px = self.maxX / self.width_km
        self.maxY = self.convert_km_to_px(self.height_km)

    def convert_lat_to_km(self, latitude):
        return latitude * self.mult

    def convert_lon_to_km(self, longitude):
        return longitude * self.mult * self.corr

    def convert_lat_to_px(self, latitude):
        return self.convert_km_to_px(self.convert_lat_to_km(latitude))

    def convert_lon_to_px(self, longitude):
        return self.convert_km_to_px(self.convert_lon_to_km(longitude))

    def convert_lat_pos_to_px(self, lat):
        return self.maxY - self.convert_km_to_px(self.convert_lat_to_km(lat - self.map.minlat))

    def convert_lon_pos_to_px(self, lon):
        return self.convert_km_to_px(self.convert_lon_to_km(lon - self.map.minlon))

    def convert_km_to_px(self, km):
        return self.factor_km_px * km

    def describe(self):
        print("Echelle de la carte")
        print("Facteur multiplicatif = {}".format(self.mult))
        print("Facteur correctif = {}".format(self.corr))
        print("Un degré de longitude fait {} km".format(self.corr * self.mult))
        print("Latitude max {}".format(self.map.maxlat))
        print("Largeur Km = {}, hauteur Km = {}".format(self.width_km, self.height_km))
        print("MaxX = {}, maxY={}".format(self.maxX, self.maxY))
        print("Facteur Km to Px : {}".format(self.factor_km_px))
