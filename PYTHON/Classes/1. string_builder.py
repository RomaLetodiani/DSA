class StringBuilder:
    # O(1)
    def __init__(self, string: str):
        self.storage = [string]
        self.length = len(string)
        self.saved = string

    # O(1)
    def append(self, string: str) -> None:
        self.storage.append(string)
        self.length += len(string)
        self.saved = None

    # O(1)
    def get_length(self) -> int:
        return self.length

    # O(N) -> O(1)
    def get_string(self) -> str:
        if self.saved:
            return self.saved
        else:
            self.saved = "".join(self.storage)
            return self.saved

def test_string_builder():
    sb = StringBuilder("abc")
    assert sb.get_length() == 3
    assert sb.get_string() == "abc"

    sb.append("defg")
    assert sb.get_length() == 7
    assert sb.get_string() == "abcdefg"
    assert sb.get_string() == "abcdefg"

    sb.append("hij")
    assert sb.get_length() == 10
    assert sb.get_string() == "abcdefghij"
    assert sb.get_string() == "abcdefghij"
    assert sb.get_string() == "abcdefghij"

    # Additional test cases
    sb.append("klmnop")
    assert sb.get_length() == 16
    assert sb.get_string() == "abcdefghijklmnop"
    assert sb.get_string() == "abcdefghijklmnop"

    sb.append("qrstuv")
    assert sb.get_length() == 22
    assert sb.get_string() == "abcdefghijklmnopqrstuv"
    assert sb.get_string() == "abcdefghijklmnopqrstuv"

    print("All test cases passed!")

test_string_builder()