from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [6],
    5: [6, 7],
    6: [],
    7: []
}
s = int(input())

visited = set()
queue = deque([s])
res = []

while queue:
    vertex = queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        res.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

n = []
for i in res:
    if i > 1 and i == 2 or i == 3 or i == 5 or i == 7 or i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        n.append(i)

l = len (n)
print(n, l)
