def unique(nums):
    new_nums = []
    new_nums.append(nums[0])
    for i in nums:
        if not i in new_nums:
            new_nums.append(i)
    return new_nums


size = int(input())
nums = []
for i in range(size):
    x = int(input())
    nums.append(x)
print(unique(nums))


