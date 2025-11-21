s = "leetcode"

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

first_unique = None
for ch in s:
    if count[ch] == 1:
        first_unique = ch
        break

    print(first_unique)