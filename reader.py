from structure import Elt, NodeElt, Way, Area, ParsedMap
from Echelle import Echelle

import xml.etree.ElementTree


def create_map_from_file(path):
    try:
        root = xml.etree.ElementTree.parse(path)
    except IOError as ex:
        print("Can't seem to be able to parse File... " + ex.strerror)
        return

    retour = ParsedMap()
    bounds = root.find("bounds")
    if bounds != None:
        retour.min_lon = float(bounds.get("minlon"))
        retour.max_lon = float(bounds.get("maxlon"))
        retour.min_lat = float(bounds.get("minlat"))
        retour.max_lat = float(bounds.get("maxlat"))
    else:
        raise Exception('Invalid format')

    nodes = {}
    for node in root.findall("node"):
        element = NodeElt(int(node.get("id")), float(node.get("lat")), float(node.get("lon")))
        for tag in node.findall("tag"):
            element.tags[tag.get("k")] = tag.get("v")
        nodes[int(node.get("id"))] = element
    retour.nodes = nodes
    ways = {}
    for way in root.findall("way"):
        element = Way(int(way.get("id")))
        element.nodes = []
        for tag in way.findall("tag"):
            element.tags[tag.get("k")] = tag.get("v")
        for nd in way.findall("nd"):
            element.nodes.append(nodes.get(int(nd.get("ref"))))
        ways[int(way.get("id"))] = element

    retour.ways = ways

    return retour

