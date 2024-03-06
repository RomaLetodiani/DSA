from ListGeneration import listGenerator
import time

arr5K = listGenerator(5000)

def bubble_sort(arr):
    for i in range(len(arr)):
        sorted = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            break

# Record the start time
start_time = time.time()

bubble_sort(arr5K)

# Record the end time
end_time = time.time()

# It will take at least 1 seconds to sort the arr5K

# if you want to visualize starting array just comment bubble_sort(arr5K) on previous lines
print(arr5K)
print('----------------------------------------------------------------')
print('// Stats of Bubble Sort //')
print('Length --> ', len(arr5K))
print("Time taken:", end_time - start_time, "seconds")