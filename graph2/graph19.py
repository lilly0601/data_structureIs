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

# Инициализация
queue = deque([start])
visited = set([start])
dist = {start: 0}      # расстояние от start
parent = {start: None} # чтобы восстановить путь

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

# Восстанавливаем путь итеративно
path = []
cur = target
while cur is not None:
    path.append(cur)
    cur = parent[cur]
path.reverse()

print("Shortest distance:", dist.get(target, None))
print("Path:", path if target in dist else None)