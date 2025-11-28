from collections import deque

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

k = int(input())
queue = deque()
queue.append((root, 1))
sum = 0

while queue:
    butaq, level_ = queue.popleft()
    print(butaq.value, level_)
    
    if level_ == k:
        sum = sum + butaq.value
        
    if butaq.left is not None:
        queue.append((butaq.left, level_ + 1))
        
    if butaq.right is not None:
        queue.append((butaq.right, level_ + 1))
        
print(sum)