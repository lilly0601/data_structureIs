text = "Айжан Ләйлә Айжан Ләйлә Айжан"

words = text.split()
counts = {}

max = 0
max_key = None

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 0


for word in counts:
    if counts[word] > max:
        max = counts[word]
        max_key = word

print(max_key)
