graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

start = 1 

stack = [start]
visited = set()
order = []

while stack:
    vertex = stack.pop()

    if vertex not in visited:
        visited.add(vertex)
        order.append(vertex)

        # Добавляем соседей в стек (в обратном порядке для корректного обхода)
        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)

print("Порядок DFS:", order)
