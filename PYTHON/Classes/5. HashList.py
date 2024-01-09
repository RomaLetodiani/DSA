class HashList:
    def __init__(self):
        self.buckets = []
        for _ in range(4):
            self.buckets.append([])
        self.length = 0

    def get_length(self) -> int:
        return self.length
    
    def append(self, string) -> None:
        index = self._get_bucket_index(string)
        self.buckets[index].append(string)
        self.length += 1

        if self.length > 2 * len(self.buckets):
            self._resize(2 * len(self.buckets))

    def contains(self, string):
        index = self._get_bucket_index(string)
        return string in self.buckets[index]
    
    def remove(self, string):
        if not self.contains(string):
            return
        
        index = self._get_bucket_index(string)
        self.buckets[index].remove(string)
        self.length -= 1

        if self.length < len(self.buckets) / 2 and len(self.buckets) > 4:
            self._resize(len(self.buckets) / 2)

    def _get_bucket_index(self, string):
        return hash(string) % len(self.buckets)
    
    def _resize(self, bucket_num: int) -> None:
        old_buckets = self.buckets
        self.buckets = []
        self.length = 0

        for _ in range(bucket_num):
            self.buckets.append([])

        for bucket in old_buckets:
            for elem in bucket:
                self.append(elem)

def test_hash_list():
    a = HashList()
    assert a.get_length() == 0
    assert a.contains("hello") == False

    # Test appending unique elements
    a.append("hello")
    assert a.get_length() == 1
    assert a.contains("hello") == True

    a.append("world")
    assert a.get_length() == 2
    assert a.contains("world") == True

    # Test removing elements
    a.remove("hello")
    assert a.get_length() == 1
    assert a.contains("hello") == False

    # Test removing non-existent element
    a.remove("foo")
    assert a.get_length() == 1  # Length shouldn't change

    # Test edge case of removing last element
    a.remove("world")
    assert a.get_length() == 0
    assert a.contains("world") == False

    # Test resizing behavior
    b = HashList()
    elements = ["apple", "banana", "cherry", "date", "elephant", "fox"]
    for element in elements:
        b.append(element)
    
    # Check before resizing
    assert b.get_length() == len(elements)

    # Test removing an element to trigger resizing
    b.remove("apple")
    assert b.get_length() == len(elements) - 1

    print("All test cases passed!")

test_hash_list()