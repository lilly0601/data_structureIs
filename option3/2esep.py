class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

nodes = [
    Node(10),
    Node(20),
    Node(30),
    Node(40),
    Node(50),
    Node(60),
    Node(70)
]

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

middle_value = find_middle(head)
print("Средний элемент связного списка:", middle_value)
