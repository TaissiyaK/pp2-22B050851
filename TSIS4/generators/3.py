def div(numbers):
    for i in numbers:
        if i%3 == 0 and i%4 == 0:
            yield i

n = int(input())
numbers = (i for i in range(n+1))
for i in div(numbers):
    print(i)