def iterative_dfs(numbers, graph):
    visited = [False] * (numbers + 1)
    count = 0

    for start in range(1, numbers + 1):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v % 2 == 0:
                    count += 1
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

    return count

n = 5
ribs = [(1,2),(1,3),(2,4),(3,5)]
graph = [[] for _ in range(n + 1)]
for a, b in ribs:
    graph[a].append(b)

print(iterative_dfs(n, graph))
