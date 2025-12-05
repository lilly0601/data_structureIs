class TreeNode:
    def __init__(self, value, left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

stack = []
current = root
res = []

while current is not None or len(stack)> 0:
    while current is not None:
        stack.append(current)
        current = current.left
        
    current= stack.pop()
    res.append(current.value)
    
    current = current.right 

n = int(input())
temp = []
for i in res:
    if i%n==0:
        temp.append(i)
if temp == []:
    print(0)
       
else:
    print(temp)
    
