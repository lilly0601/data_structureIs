# from collections import deque
# u=int(input())
# v=int(input())

# graph = {
#     1: [2, 3],
#     2: [4],
#     3: [5, 6],
#     4: [],
#     5: [],
#     6: []
# }


# # def bfs_directed(start, graph):
# queue = deque([u])
# visited = set((u,()))

# route = []
# while queue:
#     node = queue.popleft()
#     route.append(node)
#     for nei in graph[node]:
#     #    if nei is not visited:
#         for tup in visited:
#             print(tup)
#             if node == tup[0]:
#                 visited.add((node,tuple(route)))
#                 queue.append(nei)
#                 # print("yes")         

# print(visited)            

    
    
# # a = set()
# # a.add((3, ()))          
# # a.add((1, (3,)))
# # a.add((2, (3, 1)))
# # a.add((4, (3, 1, 2)))

# # print(a)

from collections import deque

# Ввод вершин
u = int(input("Стартовая вершина: "))
v = int(input("Целевая вершина: "))

graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: []
}

# очередь хранит (текущая вершина, маршрут до неё)
queue = deque([(u, (u,))])  # маршрут — кортеж
visited_vertices = set()     # просто вершины для проверки посещения
routes = set()               # множество кортежей (вершина, путь)

while queue:
    node, path = queue.popleft()
    
    if node not in visited_vertices:
        visited_vertices.add(node)
        routes.add((node, path))  # добавляем вершину и путь как кортеж
        
        for nei in graph[node]:
            if nei not in visited_vertices:
                queue.append((nei, path + (nei,)))  # создаём новый кортеж пути

# Вывод всех маршрутов
print("Все маршруты:")
for tup in routes:
    print(tup)

# Проверка наличия пути до v
found = any(tup[0] == v for tup in routes)
if found:
    print(f"Маршрут до вершины {v} существует")
else:
    print(f"Маршрут до вершины {v} НЕ существует")

