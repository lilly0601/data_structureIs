def group_anagrams(words):
    groups = {}

    for w in words:
        key = ''.join(sorted(w))
        if key not in groups:  
            groups[key] = []
        groups[key].append(w)

    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
