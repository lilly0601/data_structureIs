from collections import deque

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

start_node = 1
k = 2

visited = {start_node}
queue = deque([(start_node, 0)])
level_nodes = []

while queue:
    node, level = queue.popleft()
    
    if level == k:
        level_nodes.append(node)
    
    if level < k:
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

print(sum(level_nodes))

even_nodes = [x for x in level_nodes if x % 2 == 0]

if even_nodes:
    result = even_nodes[0]
    for x in even_nodes[1:]:
        result &= x
    print(result)
else:
    print(0)