graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [],
    5: []
}

start = 1
stack = [start]
visited = set()
res = []
cycle = False

while stack:
    v, current = stack.pop()

    if v not in visited:
        visited.add(v)
        # res.append(v)

        for u in graph[v]:
            if u not in visited:
                stack.append((u, v))
            elif u != current:
                cycle = True

print(res)

# DFS_iterative(Graph, start):
#     push(stack, start)
#     stack = пустой стек
#     visited = пустое множество


#     while stack не пуст:
#         v = pop(stack)

#         if v не в visited:
#             добавить v в visited
#             обработать(v)          // например, вывести v

#             для каждого соседа u из Graph[v]:
#                 если u не в visited:
#                     push(stack, u)
