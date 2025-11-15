class Node:
    def __init__(self,value = 0,next = None):
        self.value = value
        self.next = next

visited = set()

head = Node(value = 1)
head.next = Node(value = 2)
head.next.next = Node(value = 3)
head.next.next.next = Node(value = 4)
head.next.next.next.next = Node(value = 5)

head.next.next.next.next.next = head.next.next
current = head
is_cycle_contains = False
while current is not None:
    if current in visited:
        is_cycle_contains = True
        break
    visited.add(current)
    current = current.next
print(is_cycle_contains)
print(current)