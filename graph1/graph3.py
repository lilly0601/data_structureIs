# 3.	Вывод соседей вершины
graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

v = 1

for neighbor in graph[v]:
    print(neighbor)