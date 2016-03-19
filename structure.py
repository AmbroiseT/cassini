# Container for all Map Data
class ParsedMap:
    nodes = {}
    ways = {}
    min_lat = 0
    max_lat = 0
    min_lon = 0
    max_lon = 0

    def describe(self):
        print("Parsed Map : ")
        print("Dimensions : {} {} -> {} {}".format(self.min_lat, self.min_lon, self.max_lat, self.max_lon))
        print("Nodes : {}, ways : {}".format(len(self.nodes), len(self.ways)))


class Elt:
    id = -1
    tags = {}
    visible = True

    def __init__(self, id, visible=True):
        self.id = id
        self.visible = visible
        self.tags = {}

    @property
    def tag_keys(self):
        return self.tags.keys()


class NodeElt(Elt):
    lat = 0
    lon = 0

    def __init__(self, id, lat, lon, visible=True, ):
        super(NodeElt, self).__init__(id, visible)
        self.lat = lat
        self.lon = lon


class Way(Elt):
    nodes = []

    def __init__(self, id, visible=True, ):
        super(Way, self).__init__(id, visible)
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
            min_lon = node.lon if min_lon is None or min_lon < node.lon else min_lon

        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon
        print("Borders calculated : {} {} , {} {}".format(self.max_lon, self.max_lat, self.min_lon, self.min_lat))



    def isArea(self):
        return len(self.nodes) > 2 and self.nodes[0].id == self.nodes[-1].id


class Area(Way):
    def __init__(self, id, visible=True, ):
        super(Area, self).__init__(id, visible)
