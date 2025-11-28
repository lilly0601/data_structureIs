graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

vertex = int(input("vertex:"))

if vertex not in graph:
    print(graph)
else:

    del graph[vertex]

    for key in graph:
        graph[key].pop(vertex - 1)

print(graph)

