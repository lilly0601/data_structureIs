class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = head.next.next

visited = {}
current = head
flag = False

while current:
    if current in visited:
        flag = True
        print(current.value, flag)
        break
    visited[current] = True
    current = current.next
else:
    print(flag)




