# Nodes for different Trees

# 1. Tree
class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

# 2. Binary Tree (BT)
class BT:
    def __init__(self, value = None, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

# 3. Binary Search Tree (BST)
    # left side is less than root
    # right side is greater than root
class BST:
    def __init__(self, value = None, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right