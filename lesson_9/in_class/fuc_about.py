'''
def one():
    print('我是第一名!!!!!!!!!!!')
one()
'''

'''
def dinner():
    print('我正在吃晚饭!!!!')
dinner()
'''

'''
def sums(num1, num2):
    result = num1 + num2
    print(result)
sums(1, 2)
'''

'''
def say_hello():
    return '你好!!!!!'
print(say_hello())
'''

'''
def sub(num1, num2):
    result = num2 - num1
    return result
print(sub(5, 1))
'''

'''
lst = [-1, 20, 20.1]
print(min(lst))
print(max(lst))
print(abs(-2022))
'''

'''
def sub(num1=1,num2=3):
    result = num2- num1
    return result
print(sub(5,8))
'''

'''
print(6, 10, 'asdassadsad', [], {}, end='')  # 6 10 asdassadsad [] {}
print(6, 10, 'asdassadsad', [], {}, sep='      ')  # 6      10      asdassadsad      []      {}
'''

'''
def my_abs(num):
    if num >= 0:
        return num
    else:
        return -num
print(my_abs(-1))
'''

'''
s = '  aall'
for i in s:
    number = i.isdigit()
    letter = i.isalpha()
    space = i.isspace()
print(i.isspace())
'''

''''''
s = 'asjdrbe 12355weG w5e635'


def count(s):
    space = 0
    letter = 0
    number = 0
    for i in s:
        if i.isdigit():
            number += 1
        elif i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
    return (space, letter, number)


a = input('请输入一串字母, 我来统计各有多少字符: ')
print(count(a))
