class TreeNode:
    def __init__(self,value,left = None,right = None ):
        self.value = value
        self.left = left
        self.right = right
        
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

stack = ([root])   
res = []

while stack:
    print(stack.pop())
    node, current_sum = stack.pop()

    if not node.left and not node.right:
        res.append(current_sum)

    if node.right is not None:
        stack.append((node.right, current_sum + node.right.value))

    if node.left is not None:
        stack.append((node.left, current_sum + node.left.value))

print(res)