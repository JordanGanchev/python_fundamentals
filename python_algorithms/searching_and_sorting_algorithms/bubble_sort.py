nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for index in range(1, len(nums) - counter):
        if nums[index] < nums[index - 1]:
            nums[index], nums[index - 1] = nums[index - 1], nums[index]
            is_sorted = False
    counter += 1

print(*nums, sep=' ')

# two

# nums = [1, 3, 4, 2, 5, 6]
# for i in range(len(nums)):
#     for j in range(1, len(nums) - 1):
#         if nums[j - 1] > nums[j]:
#             nums[j], nums[j - 1] = nums[j - 1], nums[j]