a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c=[]
for i in range(10):
    temp=[]
    for j in range(20):
        temp.append(round(a[i]/(1+abs(b[j])),2))
    c.append(temp)

for row in c:
    print(row)