class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.value, end=" → ")
        current = current.next
    print("None")



l1 = Node(1, Node(3, Node(5)))
l2 = Node(2, Node(4, Node(6)))

merged = merge_sorted_lists(l1, l2)
print_list(merged)
