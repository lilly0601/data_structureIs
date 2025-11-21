list = [ 1, 2, 1, 3, 4, 1, 5]

hash = {}
res = []

for item in list:
    if item in hash:
        hash[item] += 1
    else:
        hash[item] = 1

# print(hash)
for item in hash:
    res.append(item)

print(res)
