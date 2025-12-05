graph={
    1:[1,3],
    2:[1,3,4],
    3:[1,2,4],
    4:[2,3]

}
temp=[]

for key,value in graph.items():

    for i in range(len(value)):
        temp.append((key,value[i]))



print(temp)
print(list(graph.keys()))               
