#First attempt at parsing Raw XML from OSRM
#Performances tests on finding element by id
from random import shuffle
from structure import NodeElt
from structure import ElementsABR
import time

import xml.etree.ElementTree

e = xml.etree.ElementTree.parse("data/map.osm")

#The most basic, and less optimised way to store data : a list of all elements
nodes = []



for atype in e.findall("node"):
    nodes.append(NodeElt(int(atype.get("id")), atype.get("lat"), atype.get("lon")))

print(len(nodes))


#measuring time to find elements... It's not very efficient  with a list, but we'll improve that! o(N)
start = time.clock()

match = [node for node in nodes if node.id == 3457435942]

end = time.clock()

print("Element found in "+str(end-start)+" seconds")
print("Finding all elts would take "+str((end-start) * len(nodes))+" seconds")

#Other way to store data a ordonnated tree : 
tree = ElementsABR()

#Shuffle the order of nodes, else our tree will just be a chained list => worse perfomance possible...
shuffle(nodes)
for node in nodes:
    tree.addElementIter(node)

#measuring time to find elements... With a orderred tree, it's way faster! o(log N)
#The only problem is that it takes more time to create the structure, but it's worth it!
start = time.clock()

match = tree.findById(3457435942)

end = time.clock()

print("Element found in "+str(end-start)+" seconds")
print("Finding all elts would take "+str((end-start) * len(nodes))+" seconds")

