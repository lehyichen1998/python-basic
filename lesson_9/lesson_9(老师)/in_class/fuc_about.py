'''
1: 什么是python的函数:
    函数的作用:
        提升代码的复用率；
        你想用的时候就用，不想用的时候就不用；
    # 函数的特性：
        你申明的函数 ：
        当你调用的时候才执行；
    # 函数是用来干嘛的；
        常用于封装方法；
        在需要使用到该方法的时候，进行调用；
    # 函数的基本语法：
        def 函数名():
            # 代码模块(方法体)
    # 声明一个（吃晚饭）函数:
2: 带参函数:
    def 函数名(param1,param2,.......):   #  形参
        # 方法体内接收参数
        result = param1 +param2
    # return 的 语句 作用 ；
        :return 的作用会将当前的 结果或者 值 ，返回给当前函数


3: 基本的内置函数 以及 自定义函数：
    内置的函数:
        # 不需要人为创建 ，系统自带；大多数为紫色:
        min(),max(),abs()...
        python中常用的内置函数   https://blog.csdn.net/lm_is_dc/article/details/80048400

    自定义:
        sleep()

4： 练习案例：
    统计一段字符内，存在的各种字符串

5: 总结：
    什么是函数；
    函数的使用：
        形参和实参；
        return 部分； 概念要清楚；
    自定义函数：
'''
# lst = [-1,20,20.1]
# print(abs(-100))

# 自定义函数
# def sleep():
#     print('主人您该睡觉了')
#
# sleep()

'''     模拟内置函数实现过程      '''


# 函数对象，在python 和 java ，php 面向对象 语言，一切皆为对象；
# 函数对象  和  函数是有区别的
# 演示对象:
def my_fuc():
    # 这就是方法体
    print('这是我刚定义的心函数')


# 函数对象:
print(my_fuc)  # 没有加括号执行结果:<function my_fuc at 0x00000191A5337D90>
# 通过对象进行调用，可以发现执行的是 函数的内存地址, fuc --> my_fuc --> 16进制cpu内存地址；

# 调用函数;
my_fuc()    # 调用本函数体的话，直接 执行该函数；


# help(abs)
# print() #  print(self, *args, sep=' ', end='\n', file=None):  # None

# 自定义一个我的绝对值函数:
# def my_abs(num):
#     # 实现 转换成绝对值的功能模块
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(my_abs(-1))


'''    统计一段字符内，存在的各种字符串     '''
# s = 'kakdjas  14545664a waw2123a1'  # 字母 ，数字 ，空格

# 自定义一个函数 用于分析一串字符串中存在的各种数据；
def count(s):
    # 字母出现了多少次，数字又出现了多少次，空格 出现了多少次；
    # 创建一个变量 保存对应的数据
    speace = 0
    letter = 0
    number = 0

    for i in s:  # i是一个什么对象？ 字符串对象
        if i.isdigit() :# 判断数字
            number += 1
        elif i.isalpha() :# 判断字母
            letter += 1
        elif i.isspace() :# 判断空格
            speace += 1
    return (speace,letter,number)

s = input('请输入一串字符，我来统计各有多少字符')
print(count(s))