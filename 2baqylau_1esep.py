#6-нұсқа Мөлдір 1 есеп
graph = {
    1:[2,3],
    2:[1,4,5],
    3:[1],
    4:[2],
    5:[2]
}
temp = []
for key, value in graph.items():

    for i in range(len(value)):
        temp.append((key, value[i]))
          
print(temp)
print(list(graph.keys()))
