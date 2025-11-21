nums = [1, 2, 3, 4,5,5,8]

seen = {}
for n in nums:
    if n in seen:
        print("Элементы не уникальны!")
        break
    seen[n] = True
else:
    print("Все элементы уникальны!")
