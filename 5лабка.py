numbers=[4,5,9,12,13]
m=3

count_dict={}

for r in range(m):
    count = 0
    for num in numbers:
        if num % m == r:
           count += 1
    count_dict[r]= count
   
     
    
print(count_dict)
