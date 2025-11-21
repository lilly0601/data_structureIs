A = [1, 3, 6, 7, 9]
B = [3, 10, 5, 7, 15]
k = int(input("k:"))
hash = {}

for x in A:
    if x not in hash:
        hash[x] = [0,0]
    hash[x][0] +=1

for x in B:
    if x not in hash:
        hash[x]=[0,0]
    hash[x][1] +=1

result = {}
for num, (a,b) in hash.items():
    result[num] = min(a,b) * k + abs(a-b)

print(result)