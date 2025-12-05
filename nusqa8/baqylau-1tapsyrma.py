def is_prime(x):
    if x < 2:
        return False
    for d in range(2, x):
        if x % d == 0:
            return False
    return True

adj = {
    1: [2, 3, 5],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [2, 3, ]
}

max_degree = -1
max_vertex = -1

for v in adj:
    deg = len(adj[v])
    if deg > max_degree:
        max_degree = deg
        max_vertex = v

prime_neighbors = 0
for nei in adj[max_vertex]:
    if is_prime(nei):
        prime_neighbors += 1

print(max_vertex, max_degree, prime_neighbors)
