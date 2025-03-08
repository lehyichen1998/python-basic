'''
    匿名函数
        在定义函数的时候，不想给函数起一个名字。这个时候就可以用lambda来定义一个匿名函数

        lambda这个名称来自于LISP，而LISP则是从lambda calculus(一种符号逻辑形式)取这个名称的。在Python中，
        lambda作为一个关键字，作为引入表达式的语法。想比较def函数，lambda是单一的表达式，而不是语句块!
        你仅能够在lambda中封装有限的业务逻辑，这样设计的目的:让lambda纯粹为了编写简单的函数而设计，def则
        专注于处理更大的业务。

    匿名函数的声明语法
        lambda + 参数 +表达式的方式，即：
        lambda param1,param2 : expression
        最终匿名函数会返回一个 函数对象，对象中有着函数中的结果




'''

'''   同效果 函数 和 匿名函数  '''
#   函数定义
# def add(num,num1):
#     print(num+num1)
# add(1,1)


#   匿名函数
# fuc = lambda x,y: x+y
# print(fuc(1,2,3))

# https://blog.csdn.net/Jerry_1126/article/details/40105135  # 更详细的 匿名函数参考地址；

'''  使用匿名函数解析 最大值 ，配合 max内置函数   '''


"""
    # 创建一个字典；
    dic = {'k1': 10, 'k2': 200, 'k3': 20}
    # one
    big_key = max(dic)  # 默认比较的是字典的key的大小。ASCII对于的十进制
    print(big_key)  # k3
    
    # two
    # 所以我们得自己定义一个函数 去拿到最大值；
    def func(key):
        return dic[key]
    
    ret = max(dic, key=func)  # 改变比较规则,用value比较大小，最终返回的函数是字典的key值
    print(ret)  # k2
    
    # three
    # 使用匿名函数
    ret = max(dic, key=lambda x: dic[x])
    print(ret)  # k2
"""



'''  lambda的 位置传参   '''
# lambda案例； 因为 在lambda函数中不能存在 return 语句
# print((lambda x, y: x if x > y else y)(101, 102))  # 第一种lambda 使用方式

# lambda_test = lambda x, y: x if x > y else y  # 第二种方式
# print(lambda_test(101,102))


# 等价 自定函数

# def test_fuc(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# print(test_fuc(101, 102))