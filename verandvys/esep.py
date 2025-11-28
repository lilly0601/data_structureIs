n=int(input("n:"))
n=8
m=8
a=[]
x=int(input("x:"))
degx=1
for i in range(n):
    for j in range(m):
        degx*= x
        a[i][j] = degx

for row in a:
    print(row)