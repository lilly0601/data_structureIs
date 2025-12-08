# 22.	Обнаружение цикла (неориентированный граф).
graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}
def has_cycle_undirected(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            stack = [(start, -1)]

            while stack:
                v, parent = stack.pop()
                if v in visited:
                    continue

                visited.add(v)

                for nbr in graph[v]:
                    if nbr == parent:
                        continue
                    if nbr in visited:
                        return True
                    stack.append((nbr, v))

    return False


print("Цикл есть?", has_cycle_undirected(graph))