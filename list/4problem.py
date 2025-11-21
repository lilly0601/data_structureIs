class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)  
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

current = head
matrix = []

while current:
    matrix.append(current.value)
    current = current.next

is_palindrome = True
left = 0
right = len(matrix) - 1
while left < right:
    if matrix[left] != matrix[right]:
        is_palindrome = False
        break
    left +=1
    right -=1

print(is_palindrome)
