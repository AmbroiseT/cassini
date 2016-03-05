class Elt:
    id = -1
    visible = True
    def __init__(self, id, visible=True):
        self.id = id
        self.visible = visible

    

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
        super(NodeElt, self).__init__(id, visible)
        
    
class Area(Way):
    def __init__(self, id, visible=True,):
        super(Area, self).__init__(id, visible)

node = NodeElt(1, 234, 56)
print(node)
