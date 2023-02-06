def histogram(list):
    for i in list:
        s = ''
        for j in range(i):
            s += '*'
        print(s)

size = int(input())
list = []
for i in range(size):
    x = int(input())
    list.append(x)
histogram(list)

