import random
num = random.randint(1, 20)

print('Hello! What is your name?')

name = input()

print('Well, KBTU, I am thinking of a number between 1 and 20.')
print('Take a guess.')
n = int(input())
tries = 0
if n == num:
    print(f'Good job, {name}! You guessed my number in 1 guess')
else:
    while n!=num:
        if n > num:
            print("Your guess is too high.")
            print('Take a guess.')
        elif n < num:
            print("Your guess is too high.")
            print('Take a guess.')
        n = int(input())
        tries += 1
print(f'Good job, {name}! You guessed my number in {tries} guesses!')
        
