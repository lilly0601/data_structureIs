graph = {
    1: [0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 0, 0, 0],
    3: [0, 1, 0, 1, 0, 0],
    4: [0, 0, 1, 0, 0, 1],
    5: [1, 0, 0, 0, 0, 1],
    6: [0, 0, 0, 1, 1, 0]
}

vertices = 0
edge = 0

for key in graph:
    value = graph.get(key)
    vertices = len(value)
    for i in value:
        edge += value[i]
edge = edge / 2   

print(vertices, edge)