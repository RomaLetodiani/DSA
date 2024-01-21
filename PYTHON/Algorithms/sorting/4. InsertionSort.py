from arr50K import arr50K
import time

length = len(arr50K)
middle = length // 2
arr25K = arr50K[:middle]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

# Record the start time
start_time = time.time()

sorted_arr = insertion_sort(arr25K)

# Record the end time
end_time = time.time()

# It will take at least 15 seconds to sort the arr25K

print(sorted_arr)
print('Length --> ', len(sorted_arr))
print("Time taken:", end_time - start_time, "seconds")