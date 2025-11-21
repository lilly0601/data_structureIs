nums = [5, 15, 25, 35, 45, 55, 65]
count = 0
for num in nums:
    count += 1


index = 0
for item in nums:
    if index == count // 2:
        middle = item
    index += 1

print("Орташа элемент:", middle)