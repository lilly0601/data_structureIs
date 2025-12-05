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

stack = [(root, root.value, [root.value])] # стек хранит кортеж: (узел, сумма, путь)
max_sum = 0
max_path = []

while stack:
    node, current, path = stack.pop()
    
    if not node.left and not node.right:
        if current > max_sum:
            max_sum = current
            max_path = path

    if node.right:
        stack.append((node.right, current + node.right.value, path + [node.right.value]))

    if node.left:
            stack.append((node.left, current + node.left.value, path + [node.left.value]))

print(max_sum, max_path)