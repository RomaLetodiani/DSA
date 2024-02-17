# Binary Tree (BT)
class Node:
    def __init__(self, value = None, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def print_binary_tree(node: Node) -> None:
    if not node:
        return
    
    print(node.value)
    print_binary_tree(node.left)
    print_binary_tree(node.right)

print_binary_tree(root)