# 5 нұсқа 2 есеп
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

head  = Node(value = 1)
head.next = Node(value = 2)
head.next.next = Node(value = 3)
head.next.next.next = Node(value = 4)
head.next.next.next.next = Node(value = 5)

positions =[2, 4]
current = head
product = 1
pos = 1

while current is not None:
    if pos in positions:
        product *= current.value
    current = current.next
    pos += 1

while current is not None:
    print(current.value)
    current = current.next

print(product)