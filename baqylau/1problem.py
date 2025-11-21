words = ["live", "evil"]

hash_table = {}
is_anagramma = False

for word in words:
    key = tuple(sorted(word))
    
    if key in hash_table:
        is_anagramma = True
        break
    else:
        hash_table[key] = word

print(is_anagramma)
