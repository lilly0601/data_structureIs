# 9нұсқа
class TreeArrayNode:
    def __init__(self, value, left=None, right=None):
        self.value = value  
        self.left = left
        self.right = right

root = TreeArrayNode(25)
root.left = TreeArrayNode(16)
root.right = TreeArrayNode(12)
root.left.left = TreeArrayNode(15)
root.left.right = TreeArrayNode(8)
root.right.left = TreeArrayNode(4)
root.right.right = TreeArrayNode(1)

stack = []
result = []  
current = root

while current is not None or stack:
    while current is not None:
        stack.append(current)
        current = current.left

    current = stack.pop()
    result.append(current.value)

    current = current.right

print(result)

total = 0
sign = 1
for val in result:
    total += sign * val
    sign *= -1

print(total)
