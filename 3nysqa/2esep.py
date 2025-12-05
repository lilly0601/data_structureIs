class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(12)
root.right.right = TreeNode(4)

s1 = []
s2 = []
if root is not None:
    s1.append(root)
while s1:
    u = s1.pop()
    s2.append(u)
    if u.left:
        s1.append(u.left)
    if u.right:
        s1.append(u.right)

proizvedenie = 1
zhapyraq = []
while s2:
    u = s2.pop()
    if not u.left and not u.right:
        proizvedenie *= u.v
        zhapyraq.append(u.v)

print('zhapyraq:', zhapyraq)
print('proizvedenie of zhapyraq:', proizvedenie)
