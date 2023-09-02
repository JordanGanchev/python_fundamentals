def linear_search(nums, target):
    for index, num in enumerate(nums):
        if num == target:
            return index
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 56

print(linear_search(nums, target))
