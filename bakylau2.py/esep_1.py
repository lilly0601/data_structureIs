graph = {
    1: [2],
    2: [3],
    3: [1]     
}
visited = set()
current_path = set()
cycle = False

for start in graph:
    if start in visited:
        continue
    
    stack = [start]

    while stack and not cycle:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            current_path.add(vertex)

            for nei in reversed(graph[vertex]):
                if nei in current_path:   
                    cycle = True
                    break

                if nei not in visited:
                    stack.append(nei)

        else:
            if vertex in current_path:
                current_path.remove(vertex)

    if cycle:
        break

print("Цикл бар ма:", cycle)