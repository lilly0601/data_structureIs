# 4.Добавление вершины и ребра
graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

vertex = int(input("vertex:"))

if graph.get(vertex) is not None:
    print("ондай бар", graph)

last_value_len = 0
for key, value in graph.items():
    value.append(0)
    last_value_len = len(value)

graph[vertex] = [[0] * last_value_len]

print(graph)
