# Проверка, является ли граф деревом
from collections import deque

# Проверка наличия цикла (неориентированный граф)
def has_cycle_undirected(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            queue = deque([(start, -1)])
            visited.add(start)

            while queue:
                v, parent = queue.popleft()
                for nbr in graph[v]:
                    if nbr == parent:
                        continue
                    if nbr in visited:
                        return True
                    visited.add(nbr)
                    queue.append((nbr, v))
    return False


# Проверка связности
def is_connected(graph):
    start = next(iter(graph))
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(graph[v])

    return len(visited) == len(graph)


# Проверка "дерево или нет"
def is_tree(graph):
    return is_connected(graph) and not has_cycle_undirected(graph)


# пример
graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}

print("Граф является деревом?", is_tree(graph))