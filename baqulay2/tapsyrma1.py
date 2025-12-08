graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [],
    5: []
}

adjacency_matrix = {}
v = 1
value = graph.get(v)

for v in graph:
    adjacency_matrix[v] = {}
    

