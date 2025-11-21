numbers = [21, 12, 13, 31, 4, 22]

groups = {}
for num in numbers:
    n = num
    flaq = True
    sum = 0
    while n > 0:
        qaldyq = n % 10
        n //= 10

        if flaq == True:
            sum += qaldyq
        else:
            sum -= qaldyq

        flaq = not flaq

    print(sum)
    if sum not in groups:
        groups[sum] = []     

    groups[sum].append(num)
print(groups)