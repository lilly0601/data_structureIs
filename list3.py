class Node:
    def __init__(self,value = 0,next = None):
        self.value = value
        self.next = next

arr = []

head = Node(value = 1)
head.next = Node(value = 2)
head.next.next = Node(value = 3)

current = head

while current:
    arr.append(current.value)
    current = current.next

n = len(arr)
mid = n//2

left = arr[:mid]
right = arr[mid:]

head1 = Node(left[0])
for i in range(1,len(left)):
    head1.next = Node(left[i])

head2 = Node(right[0])
for i in range(1,len(right)):
    head2.next = Node(right[i])
    
print("-*"*50
    )
current = head1 
while current is not None:
    print(current.value)
    current = current.next

print("-*"*50
    )
current = head2
while current is not None:
    print(current.value)
    current = current.next
# left,right = current(head)
print("-**"*50
    )
