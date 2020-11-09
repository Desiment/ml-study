from tree import Tree
from schoolparser import Parser
from categories import Categories

school_name = input()

parser = Parser()
tree = Tree()

data = parser.get_data(school_name)
result = tree.make_decision(data)

print(Categories.name_by_id(result))
