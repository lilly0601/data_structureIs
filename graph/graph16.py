from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

start = 1 

visited = set()
queue = deque([start])
order = []

while queue:
    vertex = queue.popleft()

    if vertex not in visited:
        visited.add(vertex)
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

print(order)
