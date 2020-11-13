import math, functools

file = open('test.in', 'r')
lines = file.readlines()
count_lines = 0

n, q, h, v = [int(i) for i in lines[count_lines].split()]
count_lines += 1
horizontals = []
verticals = []
homes = []


def transform(x, y):
    angle = math.pi / 4
    xx = x * math.cos(angle) - y * math.sin(angle)
    yy = x * math.sin(angle) + y * math.cos(angle)
    return xx, yy


def compare_x(item1, item2):
    if item1[0][0] < item2[0][0]:
        return -1
    elif item1[0][0] < item2[0][0]:
        return 1
    else:
        return 0


def compare_y(item1, item2):
    if item1[0][1] < item2[0][1]:
        return -1
    elif item1[0][1] < item2[0][1]:
        return 1
    else:
        return 0


def build(v, l, r):
    if l == r:
        tree[v] = []
        tree[v].append(homes[l])
    else:
        m = (l + r) // 2
        build(v * 2, l, m)
        build(v * 2 + 1, m + 1, r)
        tree[v] = []
        if tree[v*2] != -1:
            tree[v] = tree[v] + tree[v*2]
        if tree[v*2+1] != -1:
            tree[v] = tree[v] + tree[v*2+1]
        list.sort(tree[v], key=functools.cmp_to_key(compare_y))


def lower_bound(arr, val, coord):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m][0][coord] >= val:
            r = m
        else:
            l = m
    return r


def upper_bound(arr, val, coord):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m][0][coord] <= val:
            l = m
        else:
            r = m
    return l


def get(v, tl, tr, l, r, boty, topy):
    if l > r:
        return -1
    if tl == l and tr == r:
        ind = lower_bound(tree[v], boty, 1)
        if ind < len(tree[v]) and tree[v][ind][0][1] <= topy:
            return tree[v][ind][1]
        else:
            return -1
    else:
        tm = (tl + tr) // 2
        lres = get(v * 2, tl, tm, l, min(tm, r), boty, topy)
        rres = get(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, boty, topy)
        if lres != -1:
            return lres
        else:
            return rres


def solve(x, y):
    ldist = 0
    rdist = 4e9
    while rdist - ldist > 1e-3:
        mdist = (ldist + rdist) / 2
        lind = lower_bound(homes, x - mdist / 2, 0)
        rind = upper_bound(homes, x + mdist / 2, 0)
        if lind <= rind and get(1, 0, n - 1, lind, rind, y - mdist / 2, y + mdist / 2) != -1:
            rdist = mdist
        else:
            ldist = mdist

    lind = lower_bound(homes, x - rdist / 2, 0)
    rind = upper_bound(homes, x + rdist / 2, 0)
    return get(1, 0, n - 1, lind, rind, y - rdist / 2, y + rdist / 2)


# Input
for i in range(h):
    y = [float(i) for i in lines[count_lines].split()]
    count_lines += 1
    horizontals.append(y)

for i in range(v):
    x = [float(i) for i in lines[count_lines].split()]
    count_lines += 1
    verticals.append(x)

for i in range(n):
    x, y = [float(i) for i in lines[count_lines].split()]
    count_lines += 1
    x, y = transform(x, y)
    homes.append(((x, y), i))

# Preprocessing
homes2 = []
for el in homes: homes2.append(el)
list.sort(homes, key=functools.cmp_to_key(compare_x))

tree = []
for i in range(4 * n):
    tree.append([-1])
build(1, 0, n - 1)

for i in range(q):
    x, y = [float(i) for i in lines[count_lines].split()]
    count_lines += 1
    x, y = transform(x, y)
    ans = solve(x, y)
    print(ans+1, end=' ')
