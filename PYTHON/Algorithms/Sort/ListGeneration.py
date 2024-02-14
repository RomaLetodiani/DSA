import random

def listGenerator(size = 10000, min = -20000, max = 20000):
    return [random.randint(min, max) for _ in range(size)]