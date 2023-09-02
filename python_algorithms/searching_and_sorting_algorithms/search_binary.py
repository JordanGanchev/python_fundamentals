# 0  1  2  3  4
#[1, 2, 3, 4, 5]
#L     m       R
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid_index = (left +right) // 2
        mid_element = nums[mid_index]

        if mid_element == target:
            return mid_index
        if target > mid_element:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return -1

nums = [int(x) for x in input().split()]
target = int(input())


print(binary_search(nums, target))