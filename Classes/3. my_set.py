class MySet:
    def __init__(self):
        self.buckets = [[], [], [], []]
        self.length = 0

    def get_length(self) -> int:
        return self.length
    
    def contains(self, number: int) -> bool:
        index = self._get_bucket_index(number)
        return number in self.buckets[index]

    def add(self, number: int) -> None:
        if self.contains(number):
            return

        index = self._get_bucket_index(number)
        self.buckets[index].append(number)
        self.length += 1

    def remove(self, number: int) -> None:
        if not self.contains(number):
            return
        
        index = self._get_bucket_index(number)
        self.buckets[index].remove(number)
        self.length -= 1

    def _get_bucket_index(self, number: int) -> int:
        return hash(number) % len(self.buckets)


def test_my_set():
    my_set = MySet()
    assert my_set.get_length() == 0
    assert my_set.contains(1) == False

    my_set.add(1)
    assert my_set.get_length() == 1
    assert my_set.contains(1) == True

    my_set.add(2)
    assert my_set.get_length() == 2
    assert my_set.contains(1) == True
    assert my_set.contains(2) == True

    my_set.add(2)
    assert my_set.get_length() == 2
    assert my_set.contains(1) == True
    assert my_set.contains(2) == True

    my_set.remove(1)
    assert my_set.get_length() == 1
    assert my_set.contains(1) == False
    assert my_set.contains(2) == True

    my_set.remove(3)
    assert my_set.get_length() == 1
    assert my_set.contains(1) == False
    assert my_set.contains(2) == True

    my_set.add(10)
    my_set.add(20)
    my_set.add(30)
    my_set.add(40)
    assert my_set.get_length() == 5
    assert my_set.contains(10) == True
    assert my_set.contains(20) == True
    assert my_set.contains(30) == True
    assert my_set.contains(40) == True

    my_set.remove(20)
    assert my_set.get_length() == 4
    assert my_set.contains(20) == False

    # Test hash collisions
    class CustomHashObject:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return 1  # Force hash collision for all instances

    obj1 = CustomHashObject(1)
    obj2 = CustomHashObject(2)

    my_set.add(obj1)
    assert my_set.get_length() == 5  # Colliding hash shouldn't affect existing elements
    assert my_set.contains(obj1) == True
    assert my_set.contains(obj2) == False

    print("All test cases passed!")

test_my_set()
