def my_hash(string: str) -> int:
    hash = 0
    for ch in string:
        hash += ord(ch)
    return hash


def test_my_hash():
    assert my_hash('') == 0
    assert my_hash('a') == 97
    assert my_hash('ab') == 97 + 98
    assert my_hash('c') == 99
    assert my_hash('./?C') == my_hash('ß') # collision
    print("All test cases passed!")


test_my_hash()