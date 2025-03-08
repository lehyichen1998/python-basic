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

'''    普通函数；     '''
# def say_hello():return 'hello'
# print(say_hello())

'''     #匿名函数；      '''
# lam_fuc = lambda: 'hello'
# print(lam_fuc())

'''
匿名函数的声明语法
    lambda + 参数 + 表达式的方式(类似def 代码模块)，即：
    lambda param1,param2,param3,.... : expression
    最终匿名函数会返回一个 函数对象，对象中有着函数中的结果

'''

'''  带参的函数 和 匿名函数   '''

'''
# 整体向左 移动 ： shift+tab;
# 整理代码  ctrl+shift+alt+l; -- > code cleaup;
    # 定义普通函数
    def add(num1, num2):
        return num1 + num2
    
    
    print('add普通函数', add(1, 2))
    
    # 匿名函数
    lambda_fuc = lambda x, y: x + y
    print('匿名函数', lambda_fuc(1, 2))

'''

'''  lambda位置传参   '''
# 自定义函数
# def big_data(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
# print(big_data(66,99))

# 匿名函数实现;

# 第一种：
# lambda_fuc = lambda x,y : y if y > x else x
# print(lambda_fuc(66, 99))

# 第二种：
# print((lambda x, y: y if y > x else x)(66, 99))   # 位置传参；


'''  关于字典的一个案例  :取其中的最大值    '''
# 创建一个字典；
dc = {'k1': 10, 'k2': 30, 'k3': 20}

# print(max(dc))

# 函数读取 value
# def max_value(key):
#     return dc[key]
#
# print(max(dc,key=max_value))

# 匿名函数

print(max(dc, key=lambda x: dc[x]))





















