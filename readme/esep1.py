numbers = [18, 7, 29, 104, 56, 92, 300, 83]

def sum_of_digits(num):
    sum_value = 0
    for ch in str(num):
        sum_value += int(ch)
    return sum_value

grouped_numbers = {}

for n in numbers:
    key = sum_of_digits(n)
    grouped_numbers.setdefault(key, []).append(n)

print(f"{'Қосындысы':<12}  Сандар тізімі")
for k in sorted(grouped_numbers.keys()):
    values = ", ".join(str(v) for v in grouped_numbers[k])
    print(f"{k:<12}  {values}")