numbers = [12, 21, 33, 15, 51, 40, 4, 111]

def sum_digits(n):
    s = 0
    for digit in str(n):
        s += int(digit)
    return s

groups = {}

for num in numbers:
    s = sum_digits(num)
    if s not in groups:
        groups[s] = []
    groups[s].append(num)

print(f"{'Сумма':<10}  Сандар")
for key in sorted(groups):
    print(f"{key:<10}  {', '.join(map(str, groups[key]))}")
