nums = [int(x) for x in input().split()]

for index in range(1,len(nums)):
    for next in range(index, 0, -1):
        if nums[next] < nums[next - 1]:
            nums[next], nums[next - 1] = nums[next - 1], nums[next]
        else:
            break

print(nums)
