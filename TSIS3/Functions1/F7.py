def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            return True
    return False


nums = []
size = int(input())
for i in range(size):
    num = int(input())
    nums.append(num)
print(has_33(nums))