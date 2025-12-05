graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

seen_edges = set()
count = 0

for u in graph:
    for v in graph[u]:
        edge = tuple(sorted((u, v)))
        if edge not in seen_edges:
            print(f"({u}, {v})")
            seen_edges.add(edge)
            if (u + v) % 2 != 0:
                count += 1

print(count)