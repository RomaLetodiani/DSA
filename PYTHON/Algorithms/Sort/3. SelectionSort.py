from arr50K import arr50K
import time

length = len(arr50K)
middle = length // 2
arr25K = arr50K[:middle]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Record the start time
start_time = time.time()

sorted_arr = selection_sort(arr25K)

# Record the end time
end_time = time.time()

# It will take at least 15 seconds to sort the arr25K

print(sorted_arr)
print('Length --> ', len(arr25K))
print("Time taken:", end_time - start_time, "seconds")