from secret import neo_user, neo_passwd, neo_url
from neo4jrestclient.client import GraphDatabase
from structure import NodeElt


class NeoUtil:
    db = None

    def __int__(self):
        self.db = None

    def connect(self):
        try:
            self.db = GraphDatabase(neo_url, username=neo_user, password=neo_passwd)
        except Exception as error:
            print("Failed to connect to the database, error = {}".format(error))

    def add_nodes(self, nodes):
        node_label = self.db.labels.create("nd")
        for node in nodes:
            assert isinstance(node, NodeElt)
            node_added = self.db.nodes.create(id_elt=node.id_elt, lat=node.lat, lon=node.lon)
            node_label.add(node_added)

if __name__ == '__main__':
    neo = NeoUtil()
    neo.connect()

    node = NodeElt(2, 4, 5, True)
    neo.add_nodes([node])
