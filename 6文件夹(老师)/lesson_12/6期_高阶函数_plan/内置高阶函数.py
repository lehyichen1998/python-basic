'''
高阶内置函数
 (一) map：函数
    map(fuc,iterable,...)
    概念：map函数 第一个参数是接收一个函数对象，在后面的函数中不断的接收可迭代的序列
    并返回一个集合，并把函数的作用云因在每一个list上，最后返回作用后的新的列表结集合

 (二) filter：函数
    filter函数的简介，和语法
    主要适用于过滤，筛选掉不需要使用的函数返回符合条件的元素组成列表
    filter语法组成：
        filter(fuc,iterable)

 (三) reduce() 函数
    python3 functools
    reduce ,主要是对 变量进行乘积运算,加法，乘除
    很长的一个列表 []
    reduce 语法：
        reduce(fuc,iterable,[initilzer])
              函数   可迭代变量   实例初始值

 (四) 匿名函数：

'''
'''
(一) map：函数
    map(fuc,iterable,...)
    概念：map函数 第一个参数是接收一个函数，在后面的函数中不断的接收可迭代的序列
    并返回一个集合，并把函数的作用云因在每一个list上，最后返回作用后的新的列表结集合
    处理能力高效
'''


# map实例
def squre(a, b):
    c = a * b
    return c


num1 = [1, 2, 3, 4, 5, 20, 10]
num2 = [2, 3, 4, 5]
# 要的是函数的映射对象，而不是函数
# print('非匿名',list(map(squre,num1,num2)))#加了括号，suqre就是函数，不加括号，对象

# #lambda 匿名函数的使用
# print(list(map(lambda num1,num2:[num1*num2],[1,2,3,4,5],[2,3,4,5,16])))
'''
   map(lambda-关键字 变量1,变量2:[要执行的操作],[变量1数据],[变量二数据]) 
'''
# 效率对比##################################################
# 用时间进行判别；for  map   内推式
# for循环执行时间
'''
    import time
    times1 = time.clock()#判定cpu执行当前程序执行的时间
    lst1 = []
    for i in range(10000000):
        lst1.append(i)
    print('for循环存储使用的时间：%.9f'%float(time.clock() -times1))
    #map映射函数执行时间
    lst1.clear()
    time2 = time.clock()
    list1 = list(map(lambda x:x,range(10000000)))
    print('map映射函数耗费时间：%.9f'%float(time.clock() -time2))
    #列表推导式
    lst1.clear()
    time3 = time.clock()
    list3 = [i for i in range(10000000)]
    print('列表推导式数耗费时间：%.9f'%float(time.clock() -time3))

'''

'''
    (二)
    filter：函数
    filter函数的简介，和语法
    主要适用于过滤，筛选掉不需要使用的函数返回符合条件的元素组成列表
    filter语法组成：
    filter(old_fuc, iterable)
'''


'''
    # filter实例
    def is_odd(num):
        return num % 2 == 0
    
    
    print(list(filter(is_odd, [i for i in range(100)])))
    
    
    # filter实例 2
    def func(x): return x > 3  # 在函数中
    
    
    filter(func, [1, 2, 3, 4, 5])
    
    # filter 配合 lambda
    filter(lambda x: x > 3, [1, 2, 3, 4, 5])

'''

'''
 (三) reduce() 函数
    python3 functools
    reduce ,主要是对 变量进行乘积运算,加法，乘除
    很长的一个列表 []
    reduce 语法：
        reduce(fuc,iterable,[initilzer])
              函数   可迭代变量  实例初始值
'''
#实例
# from functools import reduce
# #来实现加法叠加的效果
# def add(a,b):
#     return a+b
#
# print(reduce(add,[1,2,3]))
# # print(list(map(add,li,lis)))
#
# from functools import reduce
# print(reduce(lambda a,b:a+b,[i for i in range(1,4)]))
