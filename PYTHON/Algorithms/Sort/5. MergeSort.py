from ListGeneration import listGenerator
import time

arr50K = listGenerator(50000)

def merge(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle_index = len(arr) // 2
    left = merge_sort(arr[:middle_index])
    right = merge_sort(arr[middle_index:])

    return merge(left, right)

# Record the start time
start_time = time.time()

sorted_arr = merge_sort(arr50K)

# Record the end time
end_time = time.time()

# It will take at least 0.1 seconds to sort the arr50K

# if you want to visualize starting array just change arr to arr50K
print(sorted_arr)
print('----------------------------------------------------------------')
print('// Stats of Merge Sort //')
print('Length --> ', len(sorted_arr))
print("Time taken:", end_time - start_time, "seconds")