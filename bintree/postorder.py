class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

stack1 = [root]
stack2 = []
res = []

#шаблон postorder
while stack1:
    current = stack1.pop()
    stack2.append(current)

    if current.left is not None:
        stack1.append(current.left)
    if current.right is not None:
        stack1.append(current.right)

while stack2:
    current = stack2.pop()
    res.append(current.value)

print(res)