import random
n=int(input("n:"))
a=[]
for i in range(n):
    temp=[]
    for j in range(9):
        temp.append(random.randint(1,100))
    a.append(temp)

for i in range(n):
   
    for j in range(9):
        if i <= j:
            a[i][j]=0

for i in range(n):
    print(a[i])