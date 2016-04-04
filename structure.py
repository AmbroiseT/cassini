# Container for all Map Data
class ParsedMap:

    def __init__(self):
        self.nodes = {}
        self.ways = {}
        self.relations = {}
        self.min_lat = 0
        self.min_lon = 0
        self.max_lat = 0
        self.max_lon = 0

    def describe(self):
        print("Parsed Map : ")
        print("Dimensions : {} {} -> {} {}".format(self.min_lat, self.min_lon, self.max_lat, self.max_lon))
        print("Nodes : {}, ways : {}".format(len(self.nodes), len(self.ways)))


class Elt:

    def __init__(self, id_elt, visible=True):
        self.id_elt = id_elt
        self.visible = visible
        self.tags = {}

    @property
    def tag_keys(self):
        return self.tags.keys()


class NodeElt(Elt):

    def __init__(self, id_elt, lat, lon, visible=True, ):
        super(NodeElt, self).__init__(id_elt, visible)
        self.lat = lat
        self.lon = lon


class Way(Elt):

    def __init__(self, id_elt, visible=True, ):
        super(Way, self).__init__(id_elt, visible)
        self.nodes = []
        self.min_lat = None
        self.min_lon = None
        self.max_lat = None
        self.max_lon = None

    def calc_borders(self):
        max_lat = None
        max_lon = None
        min_lat = None
        min_lon = None
        for node in self.nodes:
            max_lat = node.lat if max_lat is None or max_lat < node.lat else max_lat
            max_lon = node.lon if max_lon is None or max_lon < node.lon else max_lon
            min_lat = node.lat if min_lat is None or min_lat > node.lat else min_lat
            min_lon = node.lon if min_lon is None or min_lon > node.lon else min_lon

        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon

    def isArea(self):
        return len(self.nodes) > 2 and self.nodes[0].id_elt == self.nodes[-1].id_elt

    @property
    def is_river(self):
        return self.tags.get('waterway', "") == 'riverbank'


class Area(Way):
    def __init__(self, id_elt, visible=True, ):
        super(Area, self).__init__(id_elt, visible)


class Relation(Elt):

    def __init__(self, id_elt):
        super(Relation, self).__init__(id_elt)
        self.id_elt = id_elt
        self.members = []
K

