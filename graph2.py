graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: []
}

def dfs_iterative(start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)      # обработка
            visited.add(node)
            stack.extend(reversed(graph[node]))

dfs_iterative(1)
