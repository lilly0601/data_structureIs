from collections import deque

graph = {
    1: [2],
    2: [1, 3, 4],
    3: [2, 5],
    4: [2],
    5: [3, 6],
    6: []
}
start = 3

queue = deque([start])
visited = set([start])
dist = {start: 0}
parent = {start: None} 

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
            dist[neighbor] = dist[node] + 1

for key, value in graph.items():
    print(f"3 {key}: {dist.get(key, )}" )

start = 4
queue = deque([start])
visited = set([start])
dist = {start: 0}
parent = {start: None} 


while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
            dist[neighbor] = dist[node] + 1

for key, value in graph.items():
    print(f"4 {key}: {dist.get(key, )}" )



