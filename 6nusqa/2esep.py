class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def check_all_divisors_in_order(root, N):

    
    def inorder_check(node):
        if node is None:
            return True, 0 

        is_left_divisor, left_count = inorder_check(node.left)
        
        if not is_left_divisor:
            return False, 0

        current_value = node.key
        
        if current_value == 0 or N % current_value != 0:
            return False, 0 

        is_right_divisor, right_count = inorder_check(node.right)
        
        if not is_right_divisor:
            return False, 0

        total_count = left_count + 1 + right_count
        return True, total_count

    is_all_divisor, total_count = inorder_check(root)
    
    if is_all_divisor:
        return total_count
    else:
        return 0


root = Node(10)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(2)

N1 = 20
result1 = check_all_divisors_in_order(root, N1)
print(f"N={N1} үшін нәтиже (бәрі бөлгіш): {result1}") 

N2 = 12
result2 = check_all_divisors_in_order(root, N2)
print(f"N={N2} үшін нәтиже (бөлгіш еместер бар): {result2}") 