from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
target = 'F'

queue = deque([start])
visited = set([start])
dist = {start: 0}      
parent = {start: None} 

# Итеративный цикл BFS
while queue:
    node = queue.popleft()
    
    if node == target:
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
            dist[neighbor] = dist[node] + 1
            parent[neighbor] = node

path = []
cur = target
while cur is not None:
    path.append(cur)
    cur = parent[cur]
path.reverse()

print("Shortest distance:", dist.get(target, None))
print("Path:", path if target in dist else None)