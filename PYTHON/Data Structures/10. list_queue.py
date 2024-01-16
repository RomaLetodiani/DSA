from typing import Any

class ListQueue:
    # O(1)
    def __init__(self) -> None:
        self.storage = []
        self.current = 0

    # O(1)
    def size(self) -> int:
        return len(self.storage) - self.current

    # O(1) @
    def enqueue(self, value: Any) -> None:
        self.storage.append(value)

    # O(1) @
    def dequeue(self) -> Any:
        if self.current > 100:
            self.storage = self.storage[self.current: ] # O(N)
            self.current = 0
        
        self.current += 1
        return self.storage[self.current - 1]

    # O(1)
    def front(self) -> Any:
        return self.storage[self.current]

    # O(1)
    def rear(self) -> Any:
        return self.storage[-1]


def test_list_queue():
    # Create a queue
    queue = ListQueue()

    # Test enqueue method
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    assert queue.size() == 3, "Enqueue operation failed"

    # Test front and rear methods
    assert queue.front() == 5, "Front operation failed"
    assert queue.rear() == 15, "Rear operation failed"

    # Test dequeue method
    elem = queue.dequeue()
    assert elem == 5, "Dequeue operation failed"
    assert queue.size() == 2, "Dequeue operation failed"

    # Test emptying the queue
    queue.dequeue()
    queue.dequeue()
    assert queue.size() == 0, "Dequeue operation failed"

    # Test exceptions for an empty queue
    try:
        queue.dequeue()
    except IndexError as e:
        assert str(e) == "list index out of range", "Exception handling failed"

    try:
        queue.front()
    except IndexError as e:
        assert str(e) == "list index out of range", "Exception handling failed"

    try:
        queue.rear()
    except IndexError as e:
        assert str(e) == "list index out of range", "Exception handling failed"

    print("All tests passed!")

# Run the tests
test_list_queue()
