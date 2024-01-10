# @ - amortized
class MyDict:
    def __init__(self):
        self.storage = [] # [[[k,v]], [], [], []]
        for _ in range(4):
            self.storage.append([])
        self.length = 0

    def get_length(self):
        return self.length
    
    def contains(self, key: int | str):
        # bucket = self.storage[self._get_bucket_index(key)]
        # for p in bucket:
        #     if p[0] == key:
        #         return True

        return self.get(key) is not None
            
    def get(self, key: int | str):
        # if not self.contains(key):
        #     return None
        # bucket = self.storage[self._get_bucket_index(key)]
        # for p in bucket:
        #     if p[0] == key:
        #         return p[1]

        index = self._get_bucket_index(key)
        for p in self.storage[index]:
            if p[0] == key:
                return p[1]
        return None

    # O(1) @  
    def set(self, key: int | str, value: int | str):
        index = self._get_bucket_index(key)
        bucket = self.storage[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
            
        bucket.append([key, value])
        self.length += 1

        if self.length > 2 * len(self.storage):
            self._resize(2 * len(self.storage))

    def remove(self, key: int | str):
        index = self._get_bucket_index(key)
        bucket = self.storage[index]
        if self.contains(key):
            for pair in bucket:
                if pair[0] == key:
                    bucket.remove(pair)
                    self.length -= 1

            if self.length < len(self.storage) and len(self.storage) > 4:
                self._resize(len(self.storage) // 2)

    def _resize(self, bucket_nums: int):
        old_storage = self.storage
        self.storage = []
        self.length = 0

        for _ in range(bucket_nums):
            self.storage.append([])

        for old_bucket in old_storage:
            for pair in old_bucket:
                self.set(pair[0], pair[1])

    def _get_bucket_index(self, key: int | str):
        return hash(key) % len(self.storage)      

def test_my_dict():
    # Test Case 1: Creating an instance of MyDict
    my_dict = MyDict()
    assert my_dict.get_length() == 0, "Test Case 1 failed"

    # Test Case 2: Adding key-value pairs
    my_dict.set("name", "John")
    my_dict.set("age", 25)
    my_dict.set("city", "New York")
    assert my_dict.get_length() == 3, "Test Case 2 failed"
    assert my_dict.get("name") == "John", "Test Case 2 failed"
    assert my_dict.get("age") == 25, "Test Case 2 failed"
    assert my_dict.get("city") == "New York", "Test Case 2 failed"

    # Test Case 3: Updating a value
    my_dict.set("age", 26)
    assert my_dict.get_length() == 3, "Test Case 3 failed"
    assert my_dict.get("age") == 26, "Test Case 3 failed"

    # Test Case 4: Removing a key-value pair
    my_dict.remove("age")
    assert my_dict.get_length() == 2, "Test Case 4 failed"
    assert my_dict.get("age") is None, "Test Case 4 failed"

    # Test Case 5: Checking if a key exists
    assert my_dict.contains("name"), "Test Case 5 failed"
    assert not my_dict.contains("age"), "Test Case 5 failed"

    # Test Case 6: Resizing the internal storage
    for i in range(10):
        my_dict.set(f"key{i}", f"value{i}")
    assert my_dict.get_length() == 12, "Test Case 6 failed"

    # Test Case 7: Collision handling
    my_dict.set("a", "John")
    my_dict.set("b", "Alice")  # Both "a" and "b" collide
    assert my_dict.get("a") == "John", "Test Case 7 failed"
    assert my_dict.get("b") == "Alice", "Test Case 7 failed"

    # Test Case 8: Edge case for resizing (small size)
    my_dict_small = MyDict()
    for i in range(10):
        my_dict_small.set(f"key{i}", f"value{i}")
    assert my_dict_small.get_length() == 10, "Test Case 8 failed"

    # Test Case 9: Edge case for resizing (large size)
    my_dict_large = MyDict()
    for i in range(10000):
        my_dict_large.set(f"key{i}", f"value{i}")
    assert my_dict_large.get_length() == 10000, "Test Case 9 failed"

    # Test Case 10: Performance testing
    import time
    start_time = time.time()
    for i in range(10000):
        my_dict_large.set(f"key{i}", f"value{i}")
    end_time = time.time()
    print(f"Time taken to add 10000 items: {end_time - start_time} seconds") # Time taken to add 10000 items: 0.007220268249511719 seconds

    print("All test cases passed!")


# Run the test
test_my_dict()