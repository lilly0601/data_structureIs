from collections import deque

def count_connected_components(graph):
    visited = set()
    components = 0

    for vertex in graph:
        if vertex not in visited:
            # начинаем новый BFS
            queue = deque([vertex])
            visited.add(vertex)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            # после обхода всех вершин этой компоненты
            components += 1

    return components