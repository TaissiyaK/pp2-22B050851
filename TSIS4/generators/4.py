def squares(a,b):
    for i in range(a,b+1):
        yield i*i

a, b = int(input()), int(input())
for i in squares(a,b):
    print(i)

