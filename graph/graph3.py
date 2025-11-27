graph = {
    1: [0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 0, 0, 0],
    3: [0, 1, 0, 1, 0, 0],
    4: [0, 0, 1, 0, 0, 1],
    5: [1, 0, 0, 0, 0, 1],
    6: [0, 0, 0, 1, 1, 0]
}

u = 5
matrix = []
value = graph.get(u)

for i in range(len(value)):
    if value[i] == 1:
        matrix.append(i+1)   

print(matrix)
