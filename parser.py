#First attempt at parsing Raw XML from OSRM
#Performances tests on finding element by id

from structure import NodeElt
import time

import xml.etree.ElementTree

e = xml.etree.ElementTree.parse("data/map.osm")

#The most basic, and less optimised way to store data : a list of all elements
nodes = []

for atype in e.findall("node"):
    nodes.append(NodeElt(atype.get("id"), atype.get("lat"), atype.get("lon")))

print(len(nodes))

#measuring time to find elements... It's not very efficient with a list, but we'll improve that!
start = time.clock()

match = [node for node in nodes if node.id == 3457435942]

end = time.clock()

print("Element found in "+str(end-start)+" seconds")
print("Finding all elts would take "+str((end-start) * len(nodes))+" seconds")
