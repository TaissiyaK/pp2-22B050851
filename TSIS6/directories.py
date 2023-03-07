import os
# """1"""
# path = '/Users/macbookpro/Desktop/pp2-22B050851'
# dir = []
# f = []
# d_f = []
# for d in os.listdir(path):
#     if os.path.isdir(os.path.join(path, d)):
#         dir.append(d)
# print(f"Only directories: {dir}")
# for files in os.listdir(path):
#     if os.path.isfile(os.path.join(path, files)):
#         f.append(files)
# print(f"Only files: {f}")       
# for df in os.listdir(path):
#     d_f.append(df)
# print(f"All files and directories: {d_f}")
# """2"""
# path1 = '/Users/macbookpro/Desktop/pp2-22B050851/TSIS4/math/4.py'
# path2 = '/Users/macbookpro/Desktop/pp2-22B050851/TSIS6/builtin_func.py'
# print(f'Exist:{os.access(path2,os.F_OK)}')
# print(f'Readable:{os.access(path2,os.R_OK)}')
# print(f'Writable:{os.access(path2,os.W_OK)}')
# print(f'Executable:{os.access(path2,os.X_OK)}')
# """3"""
# path = '/Users/macbookpro/Desktop/pp2-22B050851/TSIS5/regex.py'
# if os.path.exists(path):
#     print(os.path.dirname(path), os.path.basename(path))
# else:
#     print('Not correct path')
# """4"""
# with open('list1.txt', 'r') as file:
#     f = file.readlines()
# lines = 0
# for i in f:
#     lines += 1
# print(f'there are {lines} lines')
# """5"""
# my_list = [1, 4, 5, 2, True]
# with open('list2.txt', 'w') as file:
#     for i in my_list:
#         file.write('%s '%i)
# with open('list2.txt', 'r') as file:
#     f = file.read()
# print(f)
# """6"""
# alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in alph:
#     f = open(f'{i}.txt', 'x')
# f.close()
# """7"""
# with open('list1.txt', 'r') as file1, open('list3.txt', 'w') as file2:
#     for i in file1.readlines():
#         file2.write(i)
# """8"""
path = '/Users/macbookpro/Desktop/pp2-22B050851/TSIS6/example.py'
if os.access(path,os.F_OK):
    os.remove(path)
        

