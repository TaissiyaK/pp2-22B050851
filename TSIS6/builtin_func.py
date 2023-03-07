"""1"""
import math
my_list = list((1,3,5,2,3))
mult = math.prod(my_list)
print(f"product is {mult}")
"""2"""
str = 'G64gjh'
sum = 0
for i in str:
    if i.isupper():
        sum += 1
    if i.islower():
        sum += 1
print(f'The sum of lower and upper cases is {sum}')
"""3"""
str1 = input()
my_list = []
for i in str1:
    my_list.append(i)
my_list.reverse()
str2 = ''.join(my_list)
if str1 == str2:
    print(f'{str1} is polindrome')
else:
    print(f'{str1} is not polindrome')
"""4"""
import time
import math
number = int(input())
miliseconds = int(input())
time.sleep(miliseconds/1000)
print(f"Square root of {number} after {miliseconds} is {math.sqrt(number)}")
"""5"""
tuple1 = (1, True, 0, 5, 10)
tuple2 = (1,True, 5, 10)
answer1 = all(tuple1)
answer2 = all(tuple2)
print(f' tuple1 is {answer1}, tuple2 is {answer2}')
