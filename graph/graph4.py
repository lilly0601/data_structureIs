graph = {
    1: [0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 0, 0, 0],
    3: [0, 1, 0, 1, 0, 0],
    4: [0, 0, 1, 0, 0, 1],
    5: [1, 0, 0, 0, 0, 1],
    6: [0, 0, 0, 1, 1, 0]
}

def add_vertex(v):
    if v not in graph:
        graph[v] = []   
    else:
        print("бар")

def add_edge(u, v):
    if u not in graph:
        add_vertex(u)
    if v not in graph:
        add_vertex(v)
    
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

add_vertex(7)
add_edge(4, 5)

print(graph)