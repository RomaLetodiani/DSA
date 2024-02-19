# Binary Search Trees (BSTs) are a type of binary tree data structure used for 
# efficient searching, insertion, and deletion operations. 
# Each node in a BST has at most two children, referred to as the left child and 
# the right child. The Binary Search Tree property ensures that for every node:
# - All nodes in the left subtree have values less than the node's value.
# - All nodes in the right subtree have values greater than the node's value.

# BSTs enable fast searching by recursively traversing the tree based on the 
# comparison of the target value with the values of nodes. Insertion and 
# deletion operations also maintain the BST property to 
# ensure that the tree remains balanced.

# BST operations have average time complexities of O(log N), 
# where N is the number of nodes in the tree. However, 
# in the worst-case scenario (unbalanced tree), 
# these operations can degrade to O(N). Various balanced BST variants, 
# such as AVL trees and Red-Black trees, address this issue by 
# automatically maintaining balance during insertion and deletion.

# For See the code example of BST visit Classes directory