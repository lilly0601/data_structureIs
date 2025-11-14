s1 = "foo"
s2 = "bar"

if len(s1) != len(s2):
    print(False)
else:
    t1 = {}
    t2 = {}
    isom = True
    
for i in range(len(s1)):
    c1 = s1[i]
    c2 = s2[i]
    if t1.get(c1) is None:
        t1[c1] = 1
    else:
        t1[c1] += 1
     
    if t2.get(c2) is None:
        t2[c2] = 1
    else:
        t2[c2] += 1

for(key, value),(key2, value2) in zip(t1.items(), t2.items()):
    if value != value2:                    
        isom = False
        
print(isom)
        
        


