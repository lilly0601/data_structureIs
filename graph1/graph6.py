# Проверка наличия петли в графе
graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

def has_loop(graph):
    for v in graph:
        if v in graph[v]:   # если вершина есть среди своих соседей → петля
            return True
    return False

print("Граф:", graph)

if has_loop(graph):
    print("Петля есть")
else:
    print("Петли нет")