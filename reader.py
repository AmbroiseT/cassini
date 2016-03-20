from structure import NodeElt, Way, ParsedMap

import xml.etree.ElementTree


def create_map_from_file(path):
    try:
        root = xml.etree.ElementTree.parse(path)
    except IOError as ex:
        print("Can't seem to be able to parse File... " + ex.strerror)
        return None
    return create_map_from_etree(root.getroot())


def create_map_with_overpass(min_lat, min_lon, max_lat, max_lon):
    """
    Uses overpass API to query all data inside the box in parameter
    :param min_lat: minimum latitude
    :param min_lon: minimum longitude
    :param max_lat: maximum latitude
    :param max_lon: maximum longitude
    :return: a Map
    """
    import overpass
    api = overpass.API()
    response = api.Get('(node({},{},{},{});<;);out;'.format(min_lat, min_lon, max_lat, max_lon))
    print(response)
    try:
        root = xml.etree.ElementTree.fromstring(response)
    except IOError as ex:
        print("Can't seem to be able to parse request... " + ex.strerror)
        return None
    return create_map_from_etree(root, min_lat, min_lon, max_lat, max_lon)


def create_map_from_etree(root, min_lat = None, min_lon = None, max_lat = None, max_lon = None):
    assert isinstance(root, xml.etree.ElementTree.Element)
    parsed_map = ParsedMap()
    bounds = root.find("bounds")
    if bounds is not None:
        parsed_map.min_lon = float(bounds.get("minlon"))
        parsed_map.max_lon = float(bounds.get("maxlon"))
        parsed_map.min_lat = float(bounds.get("minlat"))
        parsed_map.max_lat = float(bounds.get("maxlat"))
    else:
        if min_lat is not None and min_lon is not None and max_lat is not None and max_lon is not None:
            parsed_map.min_lon = min_lon
            parsed_map.max_lon = max_lon
            parsed_map.min_lat = min_lat
            parsed_map.max_lat = max_lat
        else:
            raise Exception('Invalid format')

    nodes = {}
    for node in root.findall("node"):
        element = NodeElt(int(node.get("id")), float(node.get("lat")), float(node.get("lon")))
        for tag in node.findall("tag"):
            element.tags[tag.get("k")] = tag.get("v")
        nodes[int(node.get("id"))] = element
    parsed_map.nodes = nodes
    ways = {}
    for way in root.findall("way"):
        element = Way(int(way.get("id")))
        element.nodes = []
        for tag in way.findall("tag"):
            element.tags[tag.get("k")] = tag.get("v")
        for nd in way.findall("nd"):
            recovered_node = nodes.get(int(nd.get("ref")))
            if recovered_node is not None:
                element.nodes.append(recovered_node)
        ways[int(way.get("id"))] = element
        element.calc_borders()

    parsed_map.ways = ways

    return parsed_map


if __name__ == '__main__':
    create_map_with_overpass(48.8514500, 2.2200800, 48.8527500, 2.2234300)
