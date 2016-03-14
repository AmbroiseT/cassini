import json

from structure import Elt


def palette_standard():
    """
    Returns standard colors for drawing
    """
    return {"building": 'white', "highway": 'grey', "waterway": "blue", "landuse": 'green'}


class Style:
    rules = {"default": {'color': 'black', 'visible': 'false', 'width': 0, "line-color" : 'black'}}

    def __init__(self, path="style/style1.json"):
        if path is not None:
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

    @staticmethod
    def apply(rule, element):
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

    @staticmethod
    def priority_level(rule):
        """
        Get the priority level of the rule
        :param rule: a rule ('key:value')
        :return: a number, the higher the number, the higher the priority
        """
        tab = rule.split(':')
        if len(tab) < 2:
            return 0
        else:
            priority = 0
            if tab[0] != '':
                priority += 1 if tab[0] == 'highway' else 2
            if tab[1] != '':
                priority += 3
            return priority

    def get_parameters(self, element):
        """
        Return parameters to apply to the rendering for this way
        :param element: a Way object
        :return: a dictionary containing the parameters
        """
        assert isinstance(element, Elt)
        parameter = self.rules['default'].copy()
        last_applied = 'default'
        for rule in self.rules:
            if self.apply(rule, element) and self.priority_level(rule) >= self.priority_level(last_applied):
                parameter.update(self.rules[rule])
                last_applied = rule
        return parameter


if __name__ == '__main__':
    style = Style()
    e = Elt(1234)
    e.tags = {'height': '40', 'building:part': 'yes', 'roof:orientation': 'along', 'roof:colour': '#2A2E52', 'roof:height': '10', 'roof:shape': 'mansard'}
    print(style.rules)
    print(style.get_parameters(e))
