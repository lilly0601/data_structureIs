class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

current = head
index = 1 
sum_even_pos = 0

while current:
    if index % 2 == 0:
        sum_even_pos += current.value
    current = current.next
    index += 1

print("Жұп позициядағы элементтердің қосындысы:", sum_even_pos)
