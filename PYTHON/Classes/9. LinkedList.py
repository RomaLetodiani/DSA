class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # O(1)
    def __init__(self):
        self.head = None
        self.length = 0

    # O(1)
    def size(self) -> int:
        return self.length
    
    # O(1)
    def insert_first(self, value) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    # O(N)
    def insert_last(self, value) -> None:
        if self.head is None:
            self.head = Node(value, None)
            self.length += 1
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(value, None)
            self.length += 1

    # O(N)
    def insert(self, index, value) -> None:
        if index == 0:
            self.insert_first(value)
        elif index == self.length:
            self.insert_last(value)
        else:
            cur_index = 0
            temp = self.head
            while cur_index < index - 1:
                temp = temp.next
                cur_index += 1
            temp.next = Node(value, temp.next)
            self.length += 1

    # O(N)
    def update(self, index, value) -> None:
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value

    # O(1)
    def remove_first(self) -> None:
        self.head = self.head.next
        self.length -= 1
    
    # O(N)
    def remove_last(self) -> None:
        if self.length == 1:
            self.head = None
            self.length -= 1
        else:
            temp = self.head
            for i in range(self.length - 1):
                temp = temp.next
            temp.next = None
            self.length -= 1
    
    # O(N)
    def remove_by_index(self, index) -> None:
        if index == 0:
            self.remove_first()
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1
    
    # O(N)
    def remove_by_value(self, value) -> None:
        temp = self.head
        for index in range(self.length):
            if temp.value == value:
                self.remove_by_index(index)
                return
            temp = temp.next

    # O(N)
    def print_values(self) -> None:
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

# Usage:
# ll = LinkedList()
# ll.insert_first(10)
# ll.insert_last(20)
# ll.insert(1, 15)
# ll.remove_by_index(0)
# ll.update(1, 12)
# ll.print_values()
# print(ll.size())

def test_linked_list():
    # Create a linked list
    ll = LinkedList()

    # Test insertion methods
    ll.insert_first(5)
    ll.insert_last(10)
    ll.insert(1, 7)
    ll.insert(1, 8)
    ll.insert(0, 3)

    # Test updating an element
    ll.update(3, 15)

    # Test removal methods
    ll.remove_first()
    ll.remove_last()
    ll.remove_by_value(7)
    ll.remove_by_index(1)

    # Test printing the elements
    ll.print_values()

    # Ensure the length matches expectations
    assert ll.size() == 2, "Length mismatch after operations"

    print("All tests passed!")

# Run the tests
test_linked_list()
