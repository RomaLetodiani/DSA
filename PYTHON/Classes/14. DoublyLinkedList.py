from typing import Any

class Node:
    def __init__(self, value = None, prev = None, next = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    # O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # O(1)
    def size(self) -> int:
        return self.length

    # O(1)
    def get_first(self) -> Any:
        if self.size() == 0:
            return None
        return self.head.value

    # O(1)
    def get_last(self) -> Any:
        if self.size() == 0:
            return None
        return self.tail.value

    # O(1)
    def remove_first(self) -> Any:
        first = self.get_first()

        if self.size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1

        return first

    # O(1)
    def remove_last(self) -> Any:
        last = self.get_last()

        if self.size() == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.length -= 1

        return last

    # O(1)
    def append_first(self, value) -> None:
        if self.size() == 0:
            new_node = Node(value, None, None)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1

    # O(1)
    def append_last(self, value) -> None:
        if self.size() == 0:
            new_node = Node(value, None, None)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def _get_node(self, index) -> Node:
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    # O(N)
    def get(self, index) -> Any:
        temp = self._get_node(index)
        return temp.value

    # O(N)
    def set(self, index, value) -> None:
        temp = self._get_node(index)
        temp.value = value

    # O(N)
    def remove_by_index(self, index) -> None:
        if index == 0:
            self.remove_first()
        elif index == self.size() - 1:
            self.remove_last()
        else:
            temp = self._get_node(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.length -= 1

    # O(N)
    def remove_by_value(self, value) -> None:
        # O(N)
        temp = self.head
        while temp:
            if temp.value == value:
                if temp == self.head:
                    self.remove_first()
                elif temp == self.tail:
                    self.remove_last()
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    self.length -= 1

            temp = temp.next

    # O(N)
    def insert(self, index, value) -> None:
        if index == 0:
            self.append_first(value)
        elif index == self.size():
            self.append_last(value)
        else:
            temp = self._get_node(index)
            new_node = Node(value, temp.prev, temp)
            temp.prev.next = new_node
            temp.prev = new_node
            self.length += 1

    # O(1)
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length =0

def test_doubly_linked_list():
    # Create an empty list
    dll = DoublyLinkedList()

    # Test initial state
    assert dll.size() == 0, "Size not initialized properly"
    assert dll.get_first() is None, "First element not initialized properly"
    assert dll.get_last() is None, "Last element not initialized properly"

    # Test append_first method
    dll.append_first(5)
    assert dll.size() == 1, "Append_first method failed"
    assert dll.get_first() == 5, "First element not updated properly"
    assert dll.get_last() == 5, "Last element not updated properly"

    dll.append_first(10)
    assert dll.size() == 2, "Append_first method failed"
    assert dll.get_first() == 10, "First element not updated properly"
    assert dll.get_last() == 5, "Last element not updated properly"

    # Test append_last method
    dll.append_last(15)
    assert dll.size() == 3, "Append_last method failed"
    assert dll.get_first() == 10, "First element not updated properly"
    assert dll.get_last() == 15, "Last element not updated properly"

    # Test remove_first method
    elem = dll.remove_first()
    assert elem == 10, "Remove_first method failed"
    assert dll.size() == 2, "Remove_first method failed"
    assert dll.get_first() == 5, "First element not updated properly"

    # Test remove_last method
    elem = dll.remove_last()
    assert elem == 15, "Remove_last method failed"
    assert dll.size() == 1, "Remove_last method failed"
    assert dll.get_last() == 5, "Last element not updated properly"

    # Test remove_by_index method
    dll.append_first(20)
    dll.append_last(25)
    dll.remove_by_index(1)
    assert dll.size() == 2, "Remove_by_index method failed"
    assert dll.get_first() == 20, "Remove_by_index method failed"
    assert dll.get_last() == 25, "Remove_by_index method failed"

    # Test remove_by_value method
    dll.remove_by_value(20)
    assert dll.size() == 1, "Remove_by_value method failed"
    assert dll.get_first() == 25, "Remove_by_value method failed"
    assert dll.get_last() == 25, "Remove_by_value method failed"

    # Test insert method
    dll.insert(1, 30)
    assert dll.size() == 2, "Insert method failed"
    assert dll.get_first() == 25, "Insert method failed"
    assert dll.get_last() == 30, "Insert method failed"

    # Test clear method
    dll.clear()
    assert dll.size() == 0, "Clear method failed"
    assert dll.get_first() is None, "Clear method failed"
    assert dll.get_last() is None, "Clear method failed"

    print("All tests passed!")

# Run the tests
test_doubly_linked_list()
