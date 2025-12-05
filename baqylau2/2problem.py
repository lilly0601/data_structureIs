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

stack = []
current = root
res = []
sum = 0

while current is not None or stack != []:
    while current:
        stack.append(current)
        current = current.left
    current = stack.pop()
    if current.value % 2 == 0:
        res.append(current.value)
        sum += current.value
    current = current.right

print(res, sum)