graph={
    1:[0,1],
    2:[1,0]
    }

vertex=int(input("n"))
if graph.get(vertex)is not None:


    print("ondai bar",graph)

last_value_len=0
for key,value in graph.items():
    value.append(0)
    last_value_len=len(value)
graph[vertex] = [[0]*last_value_len] 

print(graph)


# a=[[0]*4]

# print(a)