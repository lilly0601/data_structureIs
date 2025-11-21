dict1 = { 'aizhan': 1, 'lili': 2 }
dict2 = { 'lili': 1, 'aizhan':2 }

res = {}

for key, value in dict1.items():
    res[key] = value

for key, value in dict2.items():
    if key in res:
        res[key] += value
    else:
        res[key] = value

print(res)


