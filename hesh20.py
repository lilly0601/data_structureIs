word = "ббаббавф"
n = len(word)
palindrom = {}
is_even = False
is_palindrom = False

if n % 2 == 0:
    is_even = True
    
for letter in word:
    if palindrom.get(letter) is None:
        palindrom[letter] = 1
    else:
        palindrom[letter] +=1

count_odd = 0
count_even = 0
for letter, value in palindrom.items():
    if value <= 1 and count_odd < 1:
        count_odd = 1
    if value % 2 == 0:
        count_even += value

if is_even == False and len(word) - count_even == 1:
    is_palindrom = True

if is_even == True and len(word) - count_even == 0:
    is_palindrom = True

print(palindrom, count_even, count_odd, is_palindrom)