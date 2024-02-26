# A Trie, also known as a prefix tree, is a tree-like data structure used to store a 
# dynamic set of strings where the keys usually consist of characters. 
# Each node in the Trie represents a single character of the string, 
# and the edges between nodes represent the characters in the string. 
# The root of the Trie represents an empty string.

# Key Features:
# - Trie provides efficient insertion, deletion, and search operations for strings.
# - Trie is commonly used in applications requiring fast search and retrieval of strings, 
#   such as auto-complete features in text editors or search engines.

# Structure:
# - Each node in a Trie typically contains an array or a dictionary to store pointers or references to child nodes, representing characters in the string.
# - Each node also usually contains a flag to indicate whether the node represents the end of a valid string.
# - Nodes in a Trie may have varying numbers of children depending on the characters in the strings being stored.

# Operations:
# 1. Insertion: To insert a string into a Trie, traverse the Trie, creating new nodes as necessary for each character in the string.
# 2. Search: To search for a string in a Trie, traverse the Trie following the characters in the string. If the string is found, the search operation succeeds.
# 3. Deletion: To delete a string from a Trie, perform a search to locate the string in the Trie. 
   # Once found, mark the node representing the last character of the string as not representing the end of a valid string. If the node has no other children and is not the root, remove it and continue until a node with other children or that is marked as representing the end of another string is encountered.

# Advantages:
# - Trie provides efficient prefix-based operations, making it suitable for tasks such as auto-completion.
# - Trie allows for efficient storage and retrieval of strings with common prefixes, reducing memory overhead compared to other data structures.

# Disadvantages:
# - Trie may consume more memory compared to other data structures for storing a set of strings due to the overhead associated with storing individual characters at each node.
# - Implementation complexity may be higher compared to other data structures due to the need to handle variable numbers of children per node.

# Usage:
# - Trie is commonly used in applications requiring fast prefix-based operations, such as spell checkers, auto-complete features, and search engines.
# - Trie can also be used in scenarios where efficient storage and retrieval of strings with common prefixes are required.