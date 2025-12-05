class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder_iter(root):
    stack = []
    current = root
    order = []
    even_sum = 0

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        order.append(current.value)

        if current.value % 2 == 0:
            even_sum += current.value

        current = current.right

    return order, even_sum



root = Node(4,
    Node(2, Node(1), Node(3)),
    Node(6, None, Node(8))
)

order, even_sum = inorder_iter(root)

print("Inorder Traversal:", order)
print("Sum of even-valued nodes:", even_sum)
