from collections import deque

graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

in_degree = {v: 0 for v in graph}
res = []
queue = deque()


for v in graph:
    print(v)
    for neighbor in graph[v]:
        in_degree[neighbor] += 1

for v in graph:
    if in_degree[v] == 0:
        queue.append(v)
print(in_degree)

while queue:
    v = queue.popleft()
    res.append(v)

    for n in graph[v]:
        in_degree[n] -= 1
        if in_degree[n] == 0:
            queue.append(n)

if len(res) != len(graph):
    raise Exception("граф содержит цикл")

print(res)