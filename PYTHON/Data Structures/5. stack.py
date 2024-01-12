# Stack - LIFO structure (last in first out)

# size() – Returns the size of the stack
# is_empty() – Returns whether the stack is empty
# push() - Inserts the element at the top of the stack
# pop() - Returns and deletes the topmost element of the stack
# top() - Returns a reference to the topmost element of the stack

class Stack:
    # O(1)
    def __init__(self):
        self.storage = []

    # O(1)
    def size(self) -> int:
        return len(self.storage)

    # O(1)
    def is_empty(self) -> bool:
        return self.size() == 0

    # O(1) @
    def push(self, elem) -> None:
        self.storage.append(elem)

    # O(1)
    def pop(self):
        return self.storage.pop()

    # O(1)
    def top(self):
        if self.is_empty():
            return None
        return self.storage[-1]

# Usage:
# s = Stack()
# for i in range(10):
#     s.push(i)

# # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# for i in range(5):
#     print(s.pop()) # 9 8 7 6 5

# # (0, 1, 2, 3, 4)

# for i in range(5):
#     print(s.top()) # 4 4 4 4 4

# # (0, 1, 2, 3, 4)

# for i in range(5): # 4 3 2 1 0
#     print(s.pop())


def test_stack():
    # Create a stack
    stack = Stack()

    # Test is_empty method for an empty stack
    assert stack.is_empty() is True, "is_empty failed for an empty stack"

    # Test pushing multiple elements
    stack.push(5)
    assert stack.size() == 1, "Push operation failed"
    assert stack.top() == 5, "Top operation failed"

    stack.push(10)
    stack.push(15)
    assert stack.size() == 3, "Push operation failed"
    assert stack.top() == 15, "Top operation failed"

    # Test popping elements
    elem = stack.pop()
    assert elem == 15, "Pop operation failed"
    assert stack.size() == 2, "Pop operation failed"
    assert stack.top() == 10, "Top operation failed"

    elem = stack.pop()
    assert elem == 10, "Pop operation failed"
    assert stack.size() == 1, "Pop operation failed"
    assert stack.top() == 5, "Top operation failed"

    elem = stack.pop()
    assert elem == 5, "Pop operation failed"
    assert stack.size() == 0, "Pop operation failed"
    assert stack.is_empty() is True, "is_empty failed for an empty stack"

    # Try popping from an empty stack
    try:
        stack.pop()
    except IndexError:
        pass  # Expected behavior - popping from an empty stack raises an IndexError

    # Test adding elements after emptying the stack
    stack.push(20)
    stack.push(25)
    assert stack.size() == 2, "Push operation failed"
    assert stack.top() == 25, "Top operation failed"

    print("All tests passed!")

# Run the tests
# test_stack()
