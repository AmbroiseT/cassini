#Tree class used for storing/accessing elements by ID faster than with a list
class ElementsABR:
    left = None
    right = None
    value = None
    def __init__(self, value=None):
        self.value = value

    def findById(self, id):
        if self.value == None:
            return None
        if self.value.id == id :
            return self.value
        elif self.value.id < id:
            return None if self.right == None else self.right.findById(id)
        else:
            return None if self.left == None else self.left.findById(id)
    def show(self):
        if self.value == None:
            return
        if(self.left != None):
            self.left.show()
        print(self.value.id)
        if(self.right != None):
            self.right.show()
            
    def addElement(self, elt):
        if(self.value == None):
            self.value = elt
        elif self.value.id < elt.id:
            if(self.right == None):
                self.right = ElementsABR(elt)
            else:
                self.right.addElement(elt)
        else:
            if(self.left == None):
                self.left = ElementsABR(elt)
            else:
                self.left.addElement(elt)
    def addElementIter(self, elt):
        if(self.value == None):
            self.value = elt
            return
        current = self
        while(True):
            if current.value.id < elt.id:
                if(current.right == None):
                    current.right = ElementsABR(elt)
                    return
                else:
                    current = current.right
            else:
                if(current.left == None):
                    current.left = ElementsABR(elt)
                    return
                else:
                    current = current.left

#Container for all Map Data
class ParsedMap:
    nodes  = {}
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
        super(Way, self).__init__(id, visible)
        
    
class Area(Way):
    def __init__(self, id, visible=True,):
        super(Area, self).__init__(id, visible)
