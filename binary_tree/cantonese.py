from collections import deque

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

queue = deque([root])
res = []

while queue:
    node = queue.popleft()
    res.append(node.value)

    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

print(res)