class Node:
    def __init__(self,value = 0,next = None):
        self.value = value
        self.next = next

def delete_all_duplicates(head):
    current = head
    
    while head and head.next:
        if head.value == head.next.value:
            head.next = head.next.next 
        else:
            head = head.next 
        return current
        

head  = Node(value = 1)
head.next = Node(value = 1)
head.next.next = Node(value = 2)
head.next.next.next = Node(value  = 3)

newhead = delete_all_duplicates(head)        
current = newhead

while current is not None:
    print(current.value)
    current = current.next
        

    