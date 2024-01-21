from typing import List

# recursion
# Time : O(log N)
# Space : O(log N)
def BinarySearch_recursion(nums: List[int], target: int) -> int:
    return recursion_helper(nums, 0, len(nums) - 1, target)

def recursion_helper(nums, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return recursion_helper(nums, left, mid - 1, target)
    else:
        return recursion_helper(nums, mid + 1, right, target)

# while loop
# Time : O(log N)
# Space : O(1)
def BinarySearch(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Test for recursion
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_recursion = 6
result_recursion = BinarySearch_recursion(nums, target_recursion)
print(f"Recursion: Index of {target_recursion} is {result_recursion}")

# Test for while loop
target_while_loop = 3
result_while_loop = BinarySearch(nums, target_while_loop)
print(f"While Loop: Index of {target_while_loop} is {result_while_loop}")

# Test for a target not in the array
target_not_in_array = 10
result_recursion = BinarySearch_recursion(nums, target_not_in_array)
result_while_loop = BinarySearch(nums, target_not_in_array)
print(f"Recursion: Index of {target_not_in_array} is {result_recursion}")
print(f"While Loop: Index of {target_not_in_array} is {result_while_loop}")
