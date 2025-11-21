class Node:
    def __init__(self, value = 0, next=None ):
        self.value = value
        self.next = next

def check(head):
    d = head.next.val - head.val
    cur = head

    while cur.next is not None:
        if cur.next.val - cur.val != d:
            return False
        cur = cur.next
    return True

head = Node(value = 2)
head.next = Node(value = 5)
head.next.next = Node(value = 8)
head.next.next.next = Node(value = 11)

print(check(head))