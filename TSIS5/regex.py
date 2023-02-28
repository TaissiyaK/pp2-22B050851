import re

with open('row.txt') as txt:
    file = txt.read()

"""1"""
pattern = '\w*аб*\w*'
new_string1 = re.findall(pattern,file)
print('1 task', new_string1)
"""2"""
pattern = '\w*аб{2,3}\w*'
new_string2 = re.findall(pattern,file)
print('2 task', new_string2)
"""3"""
pattern = '[а-яА-Я]+-[а-я]+'
new_string3 = re.findall(pattern,file)
print('3 task', new_string3)
"""4"""
pattern = '[А-Я][а-я]+'
new_string4 = re.findall(pattern,file)
print('4 task', new_string4)
"""5"""
text = 'avvvvb nnannb'
pattern = 'a\w+b'
new_string5 = re.findall(pattern, text)
print('5 task', new_string5)
"""6"""
pattern = '[,.\s]'
new_string6 = re.sub(pattern,':',file)
print('6 task', new_string6)
"""7"""
pattern1 = '_'
text = r'some_test_text'
new_string7 = re.split(pattern1,text)
res2 = []
for i in new_string7:
    res2.append(i[0].upper() + i[1:])
print(''.join(res2))
"""8"""
text = 'YouAreNotInteresting'
pattern = r'[A-Z][^A-Z]+'
new_string8 = re.findall(pattern,text)
print('8 task',new_string8)
"""9"""
text = 'YouAreNotInteresting'
pattern = r'[A-Z][^A-Z]+'
new_string8 = re.findall(pattern,text)
str = ''
for i in new_string8:
    str += i + ' '
print(str)
"""10"""
text1 = r'TextIsThere'
pattern = r'[A-Z][^A-Z]*'
text2 = re.findall(pattern,text1)
text = []
print(text2)
for i in text2:
    text.append(i[0].lower()+i[1:])
print('10 task', '_'.join(text))

