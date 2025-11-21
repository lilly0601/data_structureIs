# нұсқа 5 1 
numbers = [152, 464, 565, 68, 321, 573]
groups = {}

for num in numbers:
    s = str(num)          
    total = 0

    if len(s) >= 1:
        total += int(s[0])      

    if len(s) >= 2:
        total += int(s[1])    

    if len(s) >= 3:
        total -= int(s[2])      

    print(num, total)

    if total not in groups:
        groups[total] = []

    groups[total].append(num)

print("\n")
print(groups)