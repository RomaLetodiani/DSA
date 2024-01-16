from typing import Any

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

class stackQueue:
    # O(1)
    def __init__(self) -> None:
        self.s1 = Stack()
        self.s2 = Stack()
        self.last = None

    # O(1)
    def size(self) -> int:
        return self.s1.size() + self.s2.size()

    # O(1)
    def enqueue(self, value: Any) -> None:
        self.s1.push(value)
        self.last = value

    # O(1) @
    def dequeue(self) -> Any:
        if self.s2.is_empty():
            self._transfer() # O(N)

        return self.s2.pop()

    # O(1) @
    def front(self) -> Any:
        if self.s2.is_empty():
            self._transfer() # O(N)
        
        return self.s2.top()

    # O(1)
    def rear(self) -> Any:
        if self.size() == 0:
            return None
        return self.last

    # O(N)
    def _transfer(self) -> None:
        while self.s1.size() > 0:
            value = self.s1.pop()
            self.s2.push(value)

def test_stack_queue():
    # Create a stackQueue
    sq = stackQueue()

    # Test initial state
    assert sq.size() == 0, "Size not initialized properly"
    assert sq.rear() is None, "Rear not initialized properly"

    # Test enqueue operations
    sq.enqueue(5)
    assert sq.size() == 1, "Enqueue operation failed"
    assert sq.front() == 5, "Front operation failed"
    assert sq.rear() == 5, "Rear operation failed"

    sq.enqueue(10)
    sq.enqueue(15)
    assert sq.size() == 3, "Enqueue operation failed"
    assert sq.front() == 5, "Front operation failed"
    assert sq.rear() == 15, "Rear operation failed"

    # Test dequeue operations
    elem = sq.dequeue()
    assert elem == 5, "Dequeue operation failed"
    assert sq.size() == 2, "Dequeue operation failed"
    assert sq.front() == 10, "Front operation failed"
    assert sq.rear() == 15, "Rear operation failed"

    elem = sq.dequeue()
    assert elem == 10, "Dequeue operation failed"
    assert sq.size() == 1, "Dequeue operation failed"
    assert sq.front() == 15, "Front operation failed"
    assert sq.rear() == 15, "Rear operation failed"

    elem = sq.dequeue()
    assert elem == 15, "Dequeue operation failed"
    assert sq.size() == 0, "Dequeue operation failed"
    assert sq.front() is None, "Front operation failed"
    assert sq.rear() is None, "Rear operation failed"

    # Try dequeueing from an empty queue
    try:
        sq.dequeue()
    except IndexError:
        pass  # Expected behavior - dequeueing from an empty queue raises an IndexError

    # Enqueue after dequeue
    sq.enqueue(20)
    sq.enqueue(25)
    assert sq.size() == 2, "Enqueue operation failed"
    assert sq.front() == 20, "Front operation failed"
    assert sq.rear() == 25, "Rear operation failed"

    print("All tests passed!")

# Run the tests
test_stack_queue()
