#1 нұсқа
dauyssyz = "бвгғджзйкқлмнңпрстфхцшщу"
words = ["бар","раб","тасу","сату","асту","балық","сөздік","құрылыс","молдир"]

hash = {}

for word in words:
    count = 0
    for letter in word:
        count += (letter in dauyssyz) 
    
    hash[count] = hash.get(count, []) + [word]

print(hash)
