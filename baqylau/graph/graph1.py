graph = {
    1: [0, 1, 1, 1],
    2: [1, 0, 1, 1],
    3: [1, 1, 0, 1],
    4: [1, 1, 1, 0]
}

vertices = 0
edge = 0

for key in graph:
    value = graph.get(key)
    vertices = len(value)
    for i in value:
        edge += value[i]
edge = edge / (vertices - 1)   

print(vertices, edge)