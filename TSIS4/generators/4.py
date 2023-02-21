def squares(numbers):
    for i in numbers:
        yield i*i

a, b = int(input()), int(input())
numbers = (i for i in range(a,b+1))
for i in squares(numbers):
    print(i)

