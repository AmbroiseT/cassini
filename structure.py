#Container for all Map Data
class ParsedMap:
	nodes = {}
	ways = {}
	minlat = 0
	maxlat = 0
	minlon = 0
	maxlon = 0
	def describe(self):
		print("Parsed Map : ")
		print("Dimensions : {} {} -> {} {}".format(self.minlat, self.minlon, self.maxlat, self.maxlon))
		print("Nodes : {}, ways : {}".format(len(self.nodes), len(self.ways)))
		

class Elt:
	id = -1
	tags = {}
	visible = True
	def __init__(self, id, visible=True):
		self.id = id
		self.visible = visible
		self.tags = {}
  
class NodeElt(Elt):
	lat = 0
	lon = 0
	def __init__(self, id, lat, lon, visible=True,):
		super(NodeElt, self).__init__(id, visible)
		self.lat = lat
		self.lon = lon

class Way(Elt):
	nodes = []
	def __init__(self, id, visible=True,):
		super(Way, self).__init__(id, visible)
		self.nodes = []
	def isArea(self):
		return len(self.nodes)>2 and self.nodes[0].id == self.nodes[-1].id 	
	
class Area(Way):
	def __init__(self, id, visible=True,):
		super(Area, self).__init__(id, visible)
