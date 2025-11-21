class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)  
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

a = 2
matrix = []
current = head

while current:
    matrix.append(current.value)  
    current = current.next    

n = len(matrix) 
i = 0
while i < len(matrix):
    if matrix[i] == a:
        matrix.pop(i)
    else:
        i += 1

# for i in range(n+1):
#     if a == matrix[i]:
#         matrix.pop(i)

        

# # print(n)

# # for i in range()    

print(matrix)

