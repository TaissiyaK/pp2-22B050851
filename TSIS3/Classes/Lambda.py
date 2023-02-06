def filter_prime(numbers):
    return filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers) 


numbers = []
size = int(input())
for i in range(size):
    x = int(input())
    numbers.append(x)
prime_numbers = list(filter_prime(numbers))
print(prime_numbers)