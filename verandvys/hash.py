class Node:
    def __init__(self, value = 0, next =None):
        self.next = next
        self.val = value

head = Node(val = 1)
head.next = Node(val = 2)
head.next.next = Node(val = 3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

n = 2 
dummy = Node(0)
dummy.next = head
first = second = dummy

for _ in range(n + 1):
    first = first.next

while first:
    first = first.next
    second = second.next

second.next = second.next.next
cur = dummy.next
while cur:
    print(cur.value, end=" -> " if cur.next else "\n")
    cur = cur.next
