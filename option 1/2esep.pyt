class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_all(head, target):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.value == target:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


result = remove_all(n1, 2)


while result:
    print(result.value, end=" -> " if result.next else "")
    result = result.next