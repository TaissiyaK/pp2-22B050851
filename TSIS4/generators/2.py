n = int(input())
numbers = (i for i in range(n+1) if i%2 == 0)
for i in numbers:
    print(i, end=' ')