'''
高阶内置函数
 (一) map：函数
    map(fuc,iterable,...)
    概念：map函数 第一个参数是接收一个函数对象，在后面的函数中不断的接收可迭代的序列
    并返回一个集合，并把函数的作用在每一个list的元素上，最后返回作用后的新的map对象结集合

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
'''

''' 
 (一) map：函数
    map(fuc,iterable,...)
    概念：map函数 第一个参数是接收一个函数对象，在后面的函数中不断的接收可迭代的序列
    并返回一个集合，并把函数的作用在每一个list的元素上，最后返回作用后的新的map对象结集合
'''
# 对一个 列表中的数据 将里面的 每个元素 实现 每个元的 2次方

# lst = [1, 2, 3]  # [1**2, 2**2, 3**2, 4**2, 5**2, 6**2]
#
# lst2 = [10, 10, 10]  # 乘积
# 普通做法
# def mult(a,b):
#     return a*b
#
# print(list(map(mult, lst,lst2)))

# lambda 使用；
# m = map(lambda num1, num2: num2 * num1, lst, lst2)
# print(list(m))


''' 
map 函数和 列表推导式 for 循环之间的效率关系    
    很多语言 都会讲究一个效率；
    java ： 程序 --> 0.1 
    python : 程序 --> 0.2 ,
'''

'''
    import time
    time1 = time.clock()    # 判定当前cpu的程序执行时间
    lst1 = []
    # 基本for 循环式
    for i in range(10000000):
        lst1.append(i)
    print('for循环的使用时间:',round(time.clock() -time1,3))
    
    # map映射式; 
    time2 = time.clock()
    lst2 = list(map(lambda x:x,range(10000000)))
    print('map映射函数使用时间:', round(time.clock() - time2,3))
    
    # 列表推导式；
    time3 = time.clock()
    lst3 = [i for i in range(10000000)]
    print('列表推导式的使用时间为:',round(time.clock() -time3,3))
'''

'''
(二)filter：函数
    filter函数的简介，和语法
    主要适用于过滤，筛选掉不需要使用的函数返回符合条件的元素组成列表
    filter语法组成：
        filter(fuc,iterable)
'''
# filter实例： 返回偶数，过滤奇数；
'''
    lst = [1, 2, 3, 4, 5, 6]
    
    # def fil(n):
    #     if n % 2 == 0:
    #         return n
    #
    # print(tuple(filter(fil, lst)))
    
    # 匿名函数的写法；
    
    # print(list(filter(lambda x: x % 2 == 0, lst)))
'''

'''
    (三) reduce() 函数
    python3 functools
    reduce ,主要是对 变量进行乘积运算,加法，乘除
    很长的一个列表 []
    reduce 语法：
        reduce(fuc,iterable,[initilzer])
              函数   可迭代变量   实例初始值
'''
# from functools import reduce
# # 实现加法叠加的效果；
# lst = [1,2,3,4,5]
# lst2 = [4,5,6]
#
# def add(a,b):
#     return a*b
#
# print(reduce(add, lst))





