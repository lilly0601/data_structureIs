list1 = [ 1, 2, 3, 4, 5]
list2 = [ 2, 5, 1, 3, 4]

hash1 = {}
hash2 = {}

for item in list1:
    hash1[item] = None

for item in list2:
    hash2[item] = None

is_flag = True
for key in hash1:
     if key not in hash2:
        is_flag = False
        break

print(is_flag)


