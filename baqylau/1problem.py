words = ["live", "evileee"]

hash_table = {}
is_anagramma = False

i = 0
while i < len(words):
    word = words[i]
    key = tuple(sorted(word))
    
    if key in hash_table:
        is_anagramma = True
        break
    else:
        hash_table[key] = word
    
    i += 1

print(is_anagramma)
