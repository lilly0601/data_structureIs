class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)  
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def stack(head,n):
    stack = []

    current = head

    while current:
        stack.append(current)
        current = current.next

    if n == len(stack):
        return head.next

    for _ in range(n):
        stack.pop()

    prev = stack[-1]
    prev.next = prev.next.next

    return head
    
def print_list(head):
    current = head
    while current:
        print(current.value, end=" → ")
        current = current.next
    print("None")

print_list(head)
head = stack(head, 2)
print_list(head)
