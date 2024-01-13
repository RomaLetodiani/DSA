# Time & Space complexity: O(M * N); M rows, N columns, M * N elems
# create
matrix = [    
    [1, 2, 3],
    [5, 6, 7],
    [9, 9, 9],
]

# Time: O(1)
# get element
# set element

# Time: O(M * N)
# iterate
for row in range(len(matrix)): # M
    for col in range(len(matrix[row])): # N
        print(matrix[row][col])

# or

for row in matrix: # M
    for elem in row: # N
        print(elem)

# Time: O(M), where M is number of rows
# insert row
a = [0, 0, 0, 0]
matrix.insert(2, a)

# Time: O(1)
# append row
a = [0, 0, 0, 0]
matrix.append(a)

# remove row
matrix.pop(0) # O(M), where M is number of rows
matrix.remove([9, 9, 9, 9]) # O(M * N)
