import random

def listGenerator(size = 10000, min = -20000, max = 20000):
    """
    Generates a list of random integers within a specified range.

    :param size: (int) The size of the list to be generated. Default is 10000.
    :param min: (int) The minimum value of the random integers to be generated. Default is -20000.
    :param max: (int) The maximum value of the random integers to be generated. Default is 20000.
    :return: (list) A list of random integers within the specified range.
    """
    return [random.randint(min, max) for _ in range(size)]


# Example usage
# Generates a list of 50000 random numbers from -1000000 to 1000000
arr_50k = listGenerator(50000, -1000000, 1000000)
print(arr_50k)
print('--------------------------------------------------------')
print('List Length:', len(arr_50k))

# Run this command in the terminal
# py .\Algorithms\Sort\ListGeneration.py