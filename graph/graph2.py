graph = {
    1: [0, 1, 1],
    2: [1, 0, 0],
    3: [1, 0, 0]
}

flag = []

v = 1

value = graph.get(v)
for i in range(len(value)):
    if value [i] == 1:
        flag.append(i + 1)

        v += 1
    
print(flag)