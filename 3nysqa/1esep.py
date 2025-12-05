n = 6
ribs = [(1,2),(2,6),(2,3),(3,4)]

graph = {str(i): [] for i in range(1, n + 1)}

for a, b in ribs:
    graph[str(a)].append(b)

print("Граф:", graph)

res = [2, 3, 4]

even_count = sum(1 for x in res if x % 2 == 0)

print("Чётные числа в res:", even_count)