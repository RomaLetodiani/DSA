from typing import Optional

class Node:
    def __init__(self) -> None:
        self.children = 26 * [None]
        self.is_ending = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()

    @staticmethod
    def _get_index(ch: str) -> int:
        return ord(ch) - ord("a")

    # Time complexity: O(N), where N is word length
    # Space complexity: O(1)
    def add(self, word: str) -> None:
        temp = self.root
        for ch in word:
            index = self._get_index(ch)
            if not temp.children[index]:
                temp.children[index] = Node()
            temp = temp.children[index]
        temp.is_ending = True

    # Time complexity: O(N), where N is word length
    # Space complexity: O(1)
    def contains_word(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            index = self._get_index(ch)
            if not temp.children[index]:
                return False
            temp = temp.children[index]
        return temp.is_ending

    # Time complexity: O(N), where N is word length
    # Space complexity: O(1)
    def contains_prefix(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            index = self._get_index(ch)
            if not temp.children[index]:
                return False
            temp = temp.children[index]
        return True

    # Time complexity: O(N), where N is word length
    # Space complexity: O(1)
    def remove(self, word: str) -> None:
        self._remove_helper(self.root, word)

    def _remove_helper(self, node: Node, word: str, depth: int = 0) -> Optional[Node]:
        if not node:
            return None
        
        if depth == len(word):
            if node.is_ending:
                node.is_ending = False
            if self._dont_have_children(node):
                node = None
            return node
        
        index = self._get_index(word[depth])
        node.children[index] = self._remove_helper(node.children[index], word, depth + 1)

        if not node.is_ending and self._dont_have_children(node):
            node = None

        return node
        
    def _dont_have_children(self, node: Node)-> bool:
        for child in node.children:
            if child:
                return False
            
        return True