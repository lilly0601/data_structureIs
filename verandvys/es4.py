a = []
for i in range(10):
    a.append((input(f"a[i+1] = ")))

b = []
for j in range(10):
    b.append((input(f"b[j+1] = ")))

c = []
for i in range(10):
    temp = []
    for j in range(10):
        temp.append(a[i] /(1 + abs(b[j])))
    c.append(temp)

for row in c:
    print(row)