class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def divide (head):
    matrix = []
    current = head

    while current:
        matrix.append(current)
        current = current.next

    n = len(matrix)
    mid = n//2

    matrix[mid - 1].next = None

    head1 = matrix[0]
    head2 = matrix[mid]

    return head1, head2

head = Node(1)  
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

left, right = divide(head)

def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

print_list(left)
print_list(right)