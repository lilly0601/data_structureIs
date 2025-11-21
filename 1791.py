from collections import deque

edges = [[1,2],[2,3],[4,2]]

queue = deque(edges)
in_degree = {}

while queue:
    u, v = queue.popleft()

    in_degree[u] = in_degree.get(u, 0) + 1
    in_degree[v] = in_degree.get(v, 0) + 1

for node, count in in_degree.items():
    if count == len(edges):  
        print(node)
        break
