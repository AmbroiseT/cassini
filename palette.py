# Juste des fonctions pour generer la map couleur<->tag pour dessiner
import json


def palette_standard():
    """
    Returns standard colors for drawing
    """
    return {"building": 'white', "highway": 'grey', "waterway": "blue", "landuse": 'green'}


class Style:
    rules = {}

    def __init_(self):
        self.rules = {}

    def import_rules_from_file(self, path):
        """
        Updates rules with the rules contained in json file
        :param path: path to the json file
        :return: void
        """
        with open(path) as json_data, json.load(json_data) as parsed:
            self.rules.update(parsed)

if __name__ == '__main__':
    style = Style()
    style.import_rules_from_file("style/style1.json")
    print(style.rules)