from typing import Any
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedQueue:
    # O(1)
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    # O(1)
    def size(self) -> int:
        return self.length

    # O(1)
    def enqueue(self, value: Any) -> None:
        if self.size() == 0:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value, None)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # O(1)
    def dequeue(self) -> Any:
        if self.size() == 0:
            raise Exception("Queue is empty!")
        
        elem = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return elem

    # O(1)
    def front(self) -> Any:
        if self.size() == 0:
            raise Exception("Queue is empty!")
            
        return self.head.value

    # O(1)
    def rear(self) -> Any:
        if self.size() == 0:
            raise Exception("Queue is empty!")
        
        return self.tail.value


def test_linked_queue():
    # Create a queue
    queue = LinkedQueue()

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
    except Exception as e:
        assert str(e) == "Queue is empty!", "Exception handling failed"

    try:
        queue.front()
    except Exception as e:
        assert str(e) == "Queue is empty!", "Exception handling failed"

    try:
        queue.rear()
    except Exception as e:
        assert str(e) == "Queue is empty!", "Exception handling failed"

    print("All tests passed!")

# Run the tests
test_linked_queue()
