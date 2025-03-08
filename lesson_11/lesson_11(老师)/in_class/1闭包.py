'''
高阶函数之
    闭包：
        将函数作为返回值这个我们称之为高阶函数
        闭包就是很典型的高阶函数
    例1：来个闭包函数,
        闭包函数定义：
            在函数内定义一个函数 返回内部函数 对象 的函数 称之为 闭包函数

'''


# 案例1；
# def out():
#     # 添加一个变量
#     a = 1
#     print('我来自外部函数')
#     def inner():
#         print('我来自内部函数', a)
#     return inner


# print(out)   # <function out at 0x000001DFE47C7D90>
# inners = out()  # 此时inners就是out函数对象\
# print(inners)   # <function out.<locals>.inner at 0x000001C3C138FBF8>
# inners()  # <function out.<locals>.inner at 0x0000019E4D0FFBF8>


'''    闭包函数最大的作用就是保证数据的安全性，以及相对数据的隐私性     '''

# 案例2
# 求平均值的函数案例；
# lst 相当于全局变量；
# lst = [10,20]   # 我们将lst 作为数据源
# def average(num):
#     lst.append(num)
#     result = sum(lst)/len(lst)     # 30 / 2
#     return result
#
#
# print(average(10))
# print(average(20))
# lst.clear()
# print(average(10))

# 通过闭包来加强lst数据的安全性；

def safety_average():
    lst = [10,20]   # 我们将lst 作为数据源
    def average(num):
        lst.append(num)
        result = sum(lst)/len(lst)     # 30 / 2
        return result
    return average

new_average = safety_average()

print(new_average(20))

'''  
总结
    函数闭包要满足三个条件：
    1：函数要相互嵌套
    2：将内部函数作为返回值返回
    3：内部函数要能使用到外部的函数对象（变量）   
    
'''


