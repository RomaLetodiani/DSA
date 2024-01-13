class MyMatrix:
    def __init__(self, rows, cols):
        self.storage = []
        for _ in range(rows):
            row = cols * [0]
            self.storage.append(row)
        self.sum = 0

    def get_n_rows(self):
        return len(self.storage)
    
    def get_n_cols(self):
        return len(self.storage[0])

    def get(self, row, col):
        return self.storage[row][col]

    def set(self, row, col, number):
        self.sum -= self.storage[row][col]
        self.storage[row][col] = number
        self.sum += number

    def contains(self, number):
        for row in self.storage:
            return number in row

    def multiply(self, k):
        for row in range(self.get_n_rows()):
            for col in range(self.get_n_cols()):
                self.storage[row][col] *= k
        self.sum *= k

    def get_sum(self):
        return self.sum

def test_my_matrix():
    matrix = MyMatrix(3, 3)
    assert matrix.get_n_rows() == 3
    assert matrix.get_n_cols() == 3
    assert matrix.get(0, 0) == 0
    assert matrix.get(0, 1) == 0
    assert matrix.get(0, 2) == 0
    assert matrix.get_sum() == 0

    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)
    matrix.set(2, 0, 7)
    matrix.set(2, 1, 8)
    matrix.set(2, 2, 9)

    assert matrix.get(0, 0) == 1
    assert matrix.get(0, 1) == 2
    assert matrix.get(0, 2) == 3
    assert matrix.get(1, 0) == 4
    assert matrix.get(1, 1) == 5
    assert matrix.get(1, 2) == 6
    assert matrix.get(2, 0) == 7
    assert matrix.get(2, 1) == 8
    assert matrix.get(2, 2) == 9
    assert matrix.contains(1) == True
    assert matrix.contains(10) == False
    assert matrix.get_sum() == 45

    # Change value 5 to 8
    matrix.set(1, 1, 8)

    assert matrix.get_sum() == 48  # New sum after changing 5 to 8

    matrix.multiply(2)
    assert matrix.get_sum() == 96

    assert matrix.get(0, 0) == 2
    assert matrix.get(0, 1) == 4
    assert matrix.get(0, 2) == 6
    assert matrix.get(1, 0) == 8
    assert matrix.get(1, 1) == 16
    assert matrix.get(1, 2) == 12
    
    print("All test cases passed!")

test_my_matrix()