def spy_game(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            new_list.append(nums[i])
    for i in range(len(new_list)-2):
        if new_list[i] == 0 and new_list[i+1] == 0 and new_list[i+2] == 7:
            return True
    return False

nums = []
size = int(input())
for i in range(size):
    x = int(input())
    nums.append(x)
print(spy_game(nums))