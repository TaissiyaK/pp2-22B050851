def convert_grams(grams):
    ounces = 28.3495231 * grams
    return ounces

def convert_in_F(F):
    C = (5 / 9) * (F - 32)
    return C

def solve(numheads, numlegs):
    d = dict()
    z = (numlegs - 2 * numheads) / 2
    k = numheads - z
    d['zaicev'] = z
    d['kur'] = k
    return d

def filter_prime(my_list):
    new_list = list()
    for i in my_list:
        if i == 2 or i == 1 or i == 3:
            new_list.append(i)
        else:
            correct = True
            for j in (2,i-1):
                if i % j == 0:
                    correct = False
            if correct:
                new_list.append(i)
    return new_list
        
def rever(sentence):
    my_list = sentence.split()
    my_list.reverse()
    s = ''
    for i in my_list:
        s += i
        s += ' '
    return s

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            return True
    return False

def spy_game(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            new_list.append(nums[i])
    for i in range(len(new_list)-2):
        if new_list[i] == 0 and new_list[i+1] == 0 and new_list[i+2] == 7:
            return True
    return False


import math
def volume(radius):
    volume = 4 / 3 * math.pi * (radius ** 3)
    return volume

def unique(nums):
    new_nums = []
    new_nums.append(nums[0])
    for i in nums:
        if not i in new_nums:
            new_nums.append(i)
    return new_nums

def palindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

def histogram(list):
    for i in list:
        s = ''
        for j in range(i):
            s += '*'
        print(s)