class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

res = [1, 2, 3, 4, 5, None, 7]
tree_nodes = []

for node_value in res:
    tree_nodes.append(TreeNode(node_value))

i = 0

for tree_node in tree_nodes:
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < len(tree_nodes):
        tree_nodes[i].left = tree_nodes[left_index]

    if right_index < len(tree_nodes):
        tree_nodes[i].right = tree_nodes[right_index]
    
    i += 1

print(tree_nodes)