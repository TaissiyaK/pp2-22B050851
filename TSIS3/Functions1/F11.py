def palindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-1-i]:
            return False
    return True


string = input()
print(palindrome(string))