from ListGeneration import listGenerator
import time

arr10K = listGenerator(10000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

# Record the start time
start_time = time.time()

insertion_sort(arr10K)

# Record the end time
end_time = time.time()

# It will take at least 2 seconds to sort the arr25K

# if you want to visualize starting array just comment insertion_sort(arr10K) on previous lines
print(arr10K)
print('----------------------------------------------------------------')
print('// Stats of Insertion Sort //')
print('Length --> ', len(arr10K))
print("Time taken:", end_time - start_time, "seconds")