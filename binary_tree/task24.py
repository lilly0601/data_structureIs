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

stack = [root]
res = []
count = 0

while stack != []:
    butaq = stack.pop()
    
    if butaq.right is not None:
        stack.append(butaq.right)
    
    if butaq.left is not None:
        stack.append(butaq.left)
        
    if butaq.right == None and butaq.left == None:
        count += 1

print(count)