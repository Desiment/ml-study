import csv
import functools
import math
import random
import pandas as pd
import matplotlib.pyplot as plt

k = 3
tests = 10

FILENAME = "../data/Iris.csv"
data = []
with open(FILENAME) as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(
            [float(row['SepalLengthCm']), float(row['SepalWidthCm']),
             float(row['PetalLengthCm']), float(row['PetalWidthCm']), row['Species']])


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


# Normalization
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
        ind = random.randint(0, len(data) - 1)
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
