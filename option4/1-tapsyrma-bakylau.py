l1 = [1, 2, 2, 3]
l2 = [2, 3, 3, 3, 4]

h = {}

for x in l1:
    h[x] = h.get(x, [0, 0])
    h[x][0] += 1

for x in l2:
    h[x] = h.get(x, [0, 0])
    h[x][1] += 1

res = {}

for x, (a, b) in h.items():
    res[x] = a*2 + b*3

print(res)