class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_all_duplicates(head):
    freq = {}
    current = head

    while current:
        freq[current.value] = freq.get(current.value, 0) + 1
        current = current.next

    dummy = Node(0)
    tail = dummy
    current = head

    while current:
        if freq[current.value] == 1:
            tail.next = Node(current.value)
            tail = tail.next
        current = current.next

    return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(4)


def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


cleaned = delete_all_duplicates(head)
print_list(cleaned)
