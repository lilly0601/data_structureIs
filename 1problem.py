words = ["live", "evil"]

hash_table = {}
is_anagramma = False

for word in words:
    count = {}
    for ch in word:
        count[ch] = count.get(ch, 0) + 1

    found = False
    for key in hash_table:
        if key == count:
            is_anagramma = True
            break
        hash_table.get(count)

print(is_anagramma)  
