from collections import defaultdict

numbers = [12, 21, 13, 31, 4]

groups = defaultdict(list)

for num in numbers:
    sum_squares = sum(int(digit)**2 for digit in str(num))
    groups[sum_squares].append(num)

for sum_sq, nums in groups.items():
    print(f"Сумма квадратов цифр = {sum_sq}: {nums}")
