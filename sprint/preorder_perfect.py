class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

stack = [root]
res = []

while stack != []:
    butaq = stack.pop()
    sum = 0
    i = 1
    while i < butaq.value:
        if butaq.value % i == 0:
            sum += i
        i += 1

    if sum == butaq.value and butaq.value != 0:
        res.append(butaq.value)


    if butaq.right is not None:
        stack.append(butaq.right)

    if butaq.left is not None:
        stack.append(butaq.left)


print(res)
# print(sum)