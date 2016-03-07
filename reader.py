from structure import Elt, NodeElt, Way, Area, ParsedMap
from Echelle import Echelle

import xml.etree.ElementTree

def createMapFromFile(path):
    try:
        parsedtree = xml.etree.ElementTree.parse(path)
    except IOError as ex:
        print("Can't seem to be able to parse File... "+ex.strerror)
        return

    retour = ParsedMap()
    bounds = parsedtree.find("bounds")
    if bounds != None:
        retour.minlon = float(bounds.get("minlon"))
        retour.maxlon = float(bounds.get("maxlon"))
        retour.minlat = float(bounds.get("minlat"))
        retour.maxlat = float(bounds.get("maxlat"))
    else:
        raise Exception('Invalid format')

    nodes = {}
    for node in parsedtree.findall("node"):
        nodes[int(node.get("id"))] = NodeElt(int(node.get("id")), float(node.get("lat")), float(node.get("lon")))

    retour.nodes = nodes

    ways = {}
    for way in parsedtree.findall("way"):
        element = Way(int(way.get("id")))
        for nd in way.findall("nd"):
            element.nodes.append(nd)
        ways[int(way.get("id"))] = element 

    retour.ways = ways

    return retour

result = createMapFromFile("data/map.osm")
print("Succesfully parsed!")
result.describe()

echelle = Echelle(result, 500)
echelle.describe()
