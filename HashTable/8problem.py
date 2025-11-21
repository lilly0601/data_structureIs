list1 = [ 1, 2, 3, 4, 5]
list2 = [ 2, 5, 1, 3, 4]

hash = {}

for item in list2:
    hash[item] = None

flag = True

for item in list1:
    if item not in hash:
        flag = False
        break 

print(hash,flag)