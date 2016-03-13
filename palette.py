import json

from structure import Elt


def palette_standard():
    """
    Returns standard colors for drawing
    """
    return {"building": 'white', "highway": 'grey', "waterway": "blue", "landuse": 'green'}


class Style:
    rules = {"default": {'color': 'black', 'visible': 'false', 'width': 0}}

    def __init__(self, path="style/style1.json"):
        if not path is None:
            self.import_rules_from_file(path)

    def import_rules_from_file(self, path):
        """
        Updates rules with the rules contained in json file
        :param path: path to the json file
        :return: void
        """
        with open(path) as json_data:
            try:
                parsed = json.load(json_data)
                self.rules.update(parsed)
            except json.JSONDecodeError:
                print("Error decoding json file!")

    def apply(self, rule, element):
        """
        Check if a rule applies to an element
        :param element Element to check
        :type rule: str
        """
        assert isinstance(rule, str)
        assert isinstance(element, Elt)
        members = rule.split(':')
        tags = element.tags
        assert isinstance(tags, dict)
        if len(members) != 2:
            return False
        if members[0] != '' and members[0] not in tags:
            return False
        if members[1] != '' and members[1] not in tags.values():
            return False
        return True

    def get_parameters(self, element):
        """
        Return parameters to apply to the rendering for this way
        :param element: a Way object
        :return: a dictionary containing the parameters
        """
        assert isinstance(element, Elt)
        parameter = self.rules['default']
        for rule in self.rules:
            if self.apply(rule, element):
                parameter.update(self.rules[rule])
        return parameter


if __name__ == '__main__':
    style = Style()
    e = Elt(1234)
    e.tags = {'building': 'park'}
    print(style.rules)
    print(style.get_parameters(e))
