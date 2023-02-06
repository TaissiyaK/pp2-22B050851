def rever(sentence):
    my_list = sentence.split()
    my_list.reverse()
    s = ''
    for i in my_list:
        s += i
        s += ' '
    return s


sentence = input()
print(rever(sentence))
