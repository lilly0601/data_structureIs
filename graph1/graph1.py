# 1️⃣ Подсчет количества вершин и рёбер
graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

u = 3
v = 2
flag = False
value = graph.get(u)

for i in range(len(value)):
    if value [v] == 1:
        flag = True

print(flag)