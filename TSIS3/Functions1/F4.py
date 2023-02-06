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
        

n = int(input())
my_list = list()
for i in range(n):
    x = int(input())
    my_list.append(x)
print(filter_prime(my_list))        


                
            