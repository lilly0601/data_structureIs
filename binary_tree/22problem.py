class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value 
        self.left = left 
        self.right = right

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

current = root
while current.left is not None:
    current = current.left

min_value = current.value
print(min_value)

current = root
while current.right is not None:
    current = current.right

max_value = current.value
print(max_value)

