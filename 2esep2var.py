#4нұсқа
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

head = Node(value = 2)
head.next = Node(value = 5)
head.next.next = Node(value = 8)
head.next.next.next = Node(value = 11)

cur = head
d = head.next.value - head.value
flag = True

while cur.next is not None:
    if cur.next.value - cur.value != d:
        flag = False
    cur = cur.next

print(flag)