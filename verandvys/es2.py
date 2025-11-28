n = int(input())
matrix = []

for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append(1 / (i + j))
    matrix.append(row)

for row in matrix:
    print(*[f"{x:.3f}" for x in row])