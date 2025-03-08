'''
lst = [1, 2, 3, 4, 5, 6]
lst2 = [10, 20, 30]
'''

'''
def mult(a,b):
    return a*b


print(list(map(mult, lst,lst2)))
'''
'''
m = map(lambda num1, num2: [num2 * num1], lst, lst2)
print(list(m))

'''

import time

'''
time1 = time.clock()
lst1 = []
for i in range(10000000):
    lst1.append(i)
print('for循环使用时间',time.clock()-time1,3)

time2 = time.clock()
lst2 = list(map(lambda x: x, range(10000000)))
print('map映射函数使用时间: ', time.clock() - time2, 3)

time3 = time.clock()
lst3 = [i for i in range(10000000)]
print('列表推导式使用时间', round(time.clock() - time3, 3))
'''

# lst = [1, 2, 3, 4, 5, 6]
'''
def fil(n):
    if n % 2 == 0:
        return n
print(tuple(filter(fil, lst)))
'''
'''
print(list(filter(lambda x: x % 2 == 0, lst)))
'''

'''
from functools import reduce
lst=[1,2,3]
lst2 = [4,5,6]

def add(a,b):
    return a+b

print(reduce(add,lst))
'''

dc = {'k1': 10, 'k2': 30, 'k3': 20}
print(max(dc.values()))


def max_value(key):
    return dc[key]


print(max(dc, key=lambda  x:dc[x]))
