from arr50K import arr50K
import time

length = len(arr50K)
middle = length // 2
arr25K = arr50K[:middle]

def bubble_sort(arr):
    for i in range(len(arr)):
        sorted = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            break

    return arr

# Record the start time
start_time = time.time()

sorted_arr = bubble_sort(arr25K)

# Record the end time
end_time = time.time()

# It will take at least 30 seconds to sort the arr25K

print(sorted_arr)
print('Length --> ', len(sorted_arr))
print("Time taken:", end_time - start_time, "seconds")