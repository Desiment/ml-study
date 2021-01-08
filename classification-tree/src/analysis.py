import pandas as pd

from tree         import Tree
from schoolparser import Parser
from categories   import Categories

parser = Parser()
tree = Tree()
count = [0, 0, 0, 0, 0, 0, 0, 0]
schools = pd.read_csv(parser.FILENAME)["FullName"].unique().tolist()
print(len(schools))
for school_name in schools:
    data = parser.get_data(school_name)
    result = tree.make_decision(data)
    count[result] += 1
print(count)
