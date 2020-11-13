import csv
import functools
import math
import random
import sys

k = 20
tests = 1

data = []
FILENAME = 'data/iris.csv'
with open(FILENAME) as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(
            [int(row['id']), float(row['sepal_length_cm']), float(row['sepal_width_cm']),
             float(row['petal_length_cm']), float(row['petal_width_cm']), row['class']])


def dist(el1, el2):
    return math.sqrt(sum([(el1[i] - el2[i]) ** 2 for i
                          in range(1, len(el1) - 1)]))


def compare(item1, item2):
    if item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    else:
        return 0


def find_knn(train, el, k):
    res = [(dist(obj, el), obj) for obj in train]
    return sorted(res, key=functools.cmp_to_key(compare))[:k]


for i in range(1, len(data[0]) - 1):
    mn = 1 << 32
    mx = -mn
    for el in data:
        mn = min(mn, el[i])
        mx = max(mx, el[i])
    for el in data:
        el[i] = el[i] / (mx - mn)

for ntest in range(tests):
    random.shuffle(data)

    bound = len(data) // 4
    train = data[:bound]
    test = data[bound:]

    total = 0
    errs = 0

    for q in range(100):
        ind = random.randint(0, len(data))
        neighbours = find_knn(train, data[ind], k)

        classes = {}
        for neighbour in neighbours:
            if neighbour[1][-1] not in classes:
                classes[neighbour[1][-1]] = 1
            else:
                classes[neighbour[1][-1]] += 1
        mx = 0
        ans = ''
        for clss in classes.keys():
            if classes[clss] > mx:
                mx = classes[clss]
                ans = clss

        if ans != data[ind][-1]:
            errs += 1
        total += 1

    print('Accuracy:', 1 - (errs / total))
