class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedStack:
    def __init__(self):
        self.head = None
        self.length = 0

    def size(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.head == None
    
    def push(self, value) -> None:
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        if self.is_empty():
            return Exception("Stack is empty!")
        
        self.length -= 1
        lastElem = self.top()
        self.head = self.head.next
        return lastElem

    def top(self):
        if self.is_empty():
            return Exception("Stack is empty!")
        
        return self.head.value

def test_linked_stack():
    # Create a LinkedStack
    lS = LinkedStack()

    # Test initial state
    assert lS.size() == 0, "Size not initialized properly"
    assert lS.is_empty() is True, "Stack should be empty initially"

    # Test pushing elements
    lS.push(5)
    lS.push(10)
    lS.push(15)

    assert lS.size() == 3, "Push operation failed"
    assert lS.is_empty() is False, "Stack should not be empty after pushing elements"
    assert lS.top() == 15, "Top element is incorrect after pushing elements"

    # Test popping elements
    popped = lS.pop()
    assert popped == 15, "Popped element should be 15"
    assert lS.size() == 2, "Pop operation failed"
    assert lS.top() == 10, "Top element is incorrect after popping elements"

    lS.pop()
    lS.pop()

    assert lS.size() == 0, "Size should be 0 after popping all elements"
    assert lS.is_empty() is True, "Stack should be empty after popping all elements"

    # Try popping from an empty stack
    try:
        lS.pop()
    except Exception as e:
        assert str(e) == "Stack is empty!", "Exception message should indicate stack is empty"

    print("All tests passed!")

# Run the tests
test_linked_stack()
