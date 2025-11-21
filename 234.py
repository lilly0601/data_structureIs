class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        arr = []

        while head:
            arr.append(head.value)
            head = head.next
        
        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1   
        return True
    
head = Node(1)  
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)