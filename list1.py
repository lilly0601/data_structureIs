class Node:
    def __init__(self,value = 0,next = None):
        self.value = value
        self.next = next


head1 = Node(value = 1)
head1.next = Node(value = 2)
head1.next.next = Node(value = 3)

head2 = Node(value = 1)
head2.next = Node(value = 1)
head2.next.next = Node(value = 2)
head2.next.next.next = Node(value = 3)
head2.next.next.next.next = Node(value = 4)

# current = head1,head2
# while current is not None:
#     print(current.value)
#     current = current.next

dummy = Node(0)
current = dummy
while head1 and head2:
    if head1.value < head2.value:
        current.next = head1
        head1 = head1.next
    else:
        current.next = head2
        head2 = head2.next
    current = current.next

current.next = head1 or head2
current = dummy

while current is not None:
    print(current.value)
    current = current.next




