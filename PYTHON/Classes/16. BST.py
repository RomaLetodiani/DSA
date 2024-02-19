class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    # Time: O(1)
    # Space: O(1)
    def __init__(self) -> None:
        self.root = None

    # Time: O(log(N)), where N is the number of nodes in the tree
    # Space: O(log(N)), where N is the number of nodes in the tree
    def contains(self, value) -> bool:
        return self._r_contains(self.root, value)
    
    def _r_contains(self, node, value) -> bool:
        if not node:
            return False
        
        if value < node.value:
            return self._r_contains(node.left, value)
        elif value > node.value:
            return self._r_contains(node.right, value)
        else:
            return True

    # Time: O(log(N)), where N is the number of nodes in the tree
    # Space: O(log(N)), where N is the number of nodes in the tree
    def insert(self, value) -> None:
        self.root = self._r_insert(self.root, value)
    
    def _r_insert(self, node, value) -> Node:
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._r_insert(node.left, value)
        elif value > node.value:
            node.right = self._r_insert(node.right, value)
        
        return node

    # Time: O(log(N)), where N is the number of nodes in the tree
    # Space: O(log(N)), where N is the number of nodes in the tree
    def delete(self, value) -> None:
        self.root = self._r_delete(self.root, value)

    def _r_delete(self, node, value) -> Node:
        if not node:
            return None

        if value < node.value:
            node.left = self._r_delete(node.left, value)
        elif value > node.value:
            node.right = self._r_delete(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.right:
                return node.left
            elif not node.left:
                return node.right
            else:
                temp = node.right
                while temp.left:
                    temp = temp.left
                right_min_value = temp.value

                node.value = right_min_value
                node.right = self._r_delete(node.right, right_min_value)

        return node


def test_binary_search_tree():
    bst = BinarySearchTree()

    # Insert elements
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Test contains
    assert bst.contains(50) == True
    assert bst.contains(90) == False

    # Delete leaf node
    bst.delete(20)
    assert bst.contains(20) == False

    # Delete node with one child
    bst.delete(30)
    assert bst.contains(30) == False
    assert bst.contains(40) == True

    # Delete node with two children
    bst.delete(70)
    assert bst.contains(70) == False
    assert bst.contains(80) == True

    print("All test cases passed!")

# Run the tests
test_binary_search_tree()
