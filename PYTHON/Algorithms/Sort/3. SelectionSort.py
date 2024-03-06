from ListGeneration import listGenerator
import time

arr10K = listGenerator(10000)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Record the start time
start_time = time.time()

selection_sort(arr10K)

# Record the end time
end_time = time.time()

# It will take at least 2 seconds to sort the arr10K

# if you want to visualize starting array just comment selection_sort(arr10K) on previous lines
print(arr10K)
print('----------------------------------------------------------------')
print('// Stats of Selection Sort //')
print('Length --> ', len(arr10K))
print("Time taken:", end_time - start_time, "seconds")