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

    def isArea(self):
        return len(self.nodes) > 2 and self.nodes[0].id == self.nodes[-1].id


class Area(Way):
    def __init__(self, id, visible=True, ):
        super(Area, self).__init__(id, visible)
