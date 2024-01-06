from typing import List

class OddEvenList:
    # Time complexity: O(1)
    def __init__(self):
        self.odds = []
        self.evens = []

    # Time complexity: O(1)
    def get_length(self) -> int:
        return len(self.odds) + len(self.evens)

    # Time complexity: O(1)
    def append(self, number: int) -> None:
        if number % 2 == 0:
            self.evens.append(number)
        else:
            self.odds.append(number)

    # Time complexity: O(1)
    def get_odd_numbers(self) -> List[int]:
        return self.odds

    # Time complexity: O(1)
    def get_even_numbers(self) -> List[int]:
        return self.evens

def test_odd_even_list() -> None:
    odd_even_list = OddEvenList()
    assert odd_even_list.get_length() == 0
    assert odd_even_list.get_odd_numbers() == []
    assert odd_even_list.get_even_numbers() == []

    odd_even_list.append(1)
    assert odd_even_list.get_length() == 1
    assert odd_even_list.get_odd_numbers() == [1]
    assert odd_even_list.get_even_numbers() == []

    odd_even_list.append(2)
    assert odd_even_list.get_length() == 2
    assert odd_even_list.get_odd_numbers() == [1]
    assert odd_even_list.get_even_numbers() == [2]

    odd_even_list.append(3)
    odd_even_list.append(4)
    odd_even_list.append(5)
    assert odd_even_list.get_length() == 5
    assert odd_even_list.get_odd_numbers() == [1, 3, 5]
    assert odd_even_list.get_even_numbers() == [2, 4]

    # Additional test cases
    odd_even_list.append(6)
    odd_even_list.append(7)
    odd_even_list.append(8)
    assert odd_even_list.get_length() == 8
    assert odd_even_list.get_odd_numbers() == [1, 3, 5, 7]
    assert odd_even_list.get_even_numbers() == [2, 4, 6, 8]

    odd_even_list.append(11)
    odd_even_list.append(22)
    assert odd_even_list.get_length() == 10
    assert odd_even_list.get_odd_numbers() == [1, 3, 5, 7, 11]
    assert odd_even_list.get_even_numbers() == [2, 4, 6, 8, 22]

    print("All test cases passed!")

test_odd_even_list()