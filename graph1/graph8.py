def degree(graph, v):
    return len(graph.get(v, []))

graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

print("Степень вершины 1:", degree(graph, 1))