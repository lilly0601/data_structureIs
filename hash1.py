import random
a = []
for i in range(10):
    a.append(random.randint(1,10))
 
n = len(a)
hash = {}
print(a)
for i in range(len(a)):
    if hash.get(a[i]) == None:
        hash[a[i]] = 1
    else:
        hash[a[i]]+=1
        
for key,value in hash.items():
    if value > 1:
        zhiylk = value
        while zhiylk > 1:
            if key in a:
                a.remove(key)
            zhiylk-=1
            
print(a)
            
        
        

    
    

# a = [1,2,2,2,3]
# if 2 in a:
#     a.remove(2)
# print(a)