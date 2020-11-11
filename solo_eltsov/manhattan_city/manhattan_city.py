n, q, h, v = [int(i) for i in input().split()]
horizontals = []
verticals = []
homes = []
queries = []

for i in range(h):
    x, y = [float(i) for i in input().split()]
    horizontals.append((x, y))

for i in range(v):
    x, y = [float(i) for i in input().split()]
    verticals.append((x, y))

for i in range(n):
    x, y = [float(i) for i in input().split()]
    homes.append((x, y))

for i in range(q):
    x, y = [float(i) for i in input().split()]
    queries.append((x, y))


