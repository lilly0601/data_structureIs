class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_right_children(root):
    if root is None:
        return 0

    total = 0

    if root.right is not None:
        total += root.right.value

    total += sum_right_children(root.left)
    total += sum_right_children(root.right)

    return total


root = Node(10,
    Node(5, Node(2), Node(7)),
    Node(15, Node(13), Node(20))
)

print(sum_right_children(root))
