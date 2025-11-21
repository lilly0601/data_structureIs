text1 = "leetcode"
text2 = "leetcode"

words1 = text1.split()
words2 = text2.split()

count1 = {}
count2 = {}

flag = True

for ch in words1:
    if ch in count1:
        count1[ch] += 1
    else:
        count1[ch] = 0

for ch in words2:
    if ch in count2:
        count2[ch] += 1
    else:
        count2[ch] = 0

for key in count1:
    if  key not in count2 or count1[key] != count2[key]:
        flag = False

print(flag)
