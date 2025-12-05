from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(12)
root.left = TreeNode(6)
root.right = TreeNode(18)
root.left.left = TreeNode(3)
root.left.right = TreeNode(9)
root.right.left = TreeNode(15)
root.right.right = TreeNode(21)

queue = deque([root])
count = 0

while queue:
    node = queue.popleft()
    if node.value % 3 == 0 or node.value % 5 == 0 or node.value % 7 == 0:
        count += 1
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

print("3, 5 және 7-ге еселі түйіндер саны:", count)