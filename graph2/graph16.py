# Реализуйте BFS и выведите порядок обхода вершин.
from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

def bfs(graph, start):
    visited = set()            
    queue = deque([start])     
    order = []                 

    while queue:
        vertex = queue.popleft()     
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)

            # добавляем всех соседей в очередь
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order


print(bfs(graph, 1))   