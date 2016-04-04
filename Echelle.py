import math
from structure import ParsedMap, Way


class Echelle:
    # Facteur multiplicatif pour faire une projection des coords
    mult = 40000 / 360

    def __init__(self, map, maxX=500):
        assert isinstance(map, ParsedMap)
        self.maxX = maxX
        self.map = map
        self.zoom = 1
        self.corr = math.cos(math.radians(self.map.max_lat))
        self.height_km = self.convert_lat_to_km(self.map.max_lat - self.map.min_lat)
        self.width_km = self.convert_lon_to_km(self.map.max_lon - self.map.min_lon)
        self.factor_km_px = self.maxX / self.width_km
        self.maxY = self.convert_km_to_px(self.height_km)
        self.corner = (0, 0)

    # Distance converters
    def convert_lat_to_km(self, latitude):
        return latitude * self.mult

    def convert_lon_to_km(self, longitude):
        return longitude * self.mult * self.corr

    def convert_lat_to_px(self, latitude):
        return self.convert_km_to_px(self.convert_lat_to_km(latitude)) * self.zoom

    def convert_lon_to_px(self, longitude):
        return self.convert_km_to_px(self.convert_lon_to_km(longitude)) * self.zoom

    def convert_km_to_px(self, km):
        return self.factor_km_px * km * self.zoom

    def convert_px_to_km(self, px):
        return px / (self.factor_km_px * self.zoom)

    # Position converters
    def convert_lat_pos_to_px(self, lat):
        return self.maxY - self.convert_km_to_px_y(self.convert_lat_to_km(lat - self.map.min_lat))

    def convert_lon_pos_to_px(self, lon):
        return self.convert_km_to_px_x(self.convert_lon_to_km(lon - self.map.min_lon))

    def convert_km_to_px_x(self, km):
        return self.factor_km_px * (km + self.corner[0]) * self.zoom

    def convert_km_to_px_y(self, km):
        return self.factor_km_px * (self.corner[1] + km) * self.zoom

    def is_to_draw(self, way):
        """
        Method used to know if a certain element should be drawn on the screen (ie if it is inside the frame)
        :param way: the element
        :return: True if the element should be drawn
        """
        assert isinstance(way, Way)
        return not ((0 > self.convert_lon_pos_to_px(way.max_lon)) or
                    (self.maxX < self.convert_lon_pos_to_px(way.min_lon)) or
                    (0 > self.convert_lat_pos_to_px(way.min_lat)) or
                    (self.maxY < self.convert_lat_pos_to_px(way.max_lat)))

    def is_too_small(self, way):
        """
        Method used to check if an element is too small to be drawn on the map
        :param way:
        :return:
        """
        assert isinstance(way, Way)
        area = (self.convert_lat_pos_to_px(way.min_lat) - self.convert_lat_pos_to_px(way.max_lat)) *\
               (self.convert_lon_pos_to_px(way.max_lon) - self.convert_lon_pos_to_px(way.min_lon))
        return area < (self.maxX*self.maxY)/2000

    def describe(self):
        print("Echelle de la carte")
        print("Facteur multiplicatif = {}".format(self.mult))
        print("Facteur correctif = {}".format(self.corr))
        print("Un degré de longitude fait {} km".format(self.corr * self.mult))
        print("Latitude max {}".format(self.map.max_lat))
        print("Largeur Km = {}, hauteur Km = {}".format(self.width_km, self.height_km))
        print("MaxX = {}, maxY={}".format(self.maxX, self.maxY))
        print("Facteur Km to Px : {}".format(self.factor_km_px))
