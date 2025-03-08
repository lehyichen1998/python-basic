'''
高阶函数之
    闭包：
        将函数作为返回值这个我们称之为高阶函数
        闭包就是很典型的高阶函数
    例1：来个闭包函数,
        闭包函数定义：
            在函数内定义一个函数 返回内部函数 对象 的函数 称之为 闭包函数

'''


# 例1：
def out():
    # 定义个变量
    a = 1
    print('我来自外层函数')

    def inner():
        print('我来自内层函数', a)

    # 将内部函数作为返回值返回给外层函数out
    return inner


# 调用一下
# out()
# 我们发现我们根本拿不到里面的inner函数，只是为什么呢？应为我们现在是定义的闭包函数
# 那么我们这样遍历这个函数有什么用呢?#在程序中我们有有些数据只有编写的这个人知道，
# 而别人不知道，这样在某种程度上具备有一定的安全性

# 当然要拿还是可以拿出来的,将out函数 对象值传递给 一个新的实例对象，进行调用
o = out()
o()


# 这时候我们已近可以拿出里面的函数了

# 举个实用例子
# nums = [10,20,30]
# def average(n):
#     nums.append(n)
#     return sum(nums)/len(nums)

# print(average(10))
# 那么问题来了，因为我是一个普通函数可以随意修改,为了边这种情况我们要来个闭包保障数据安全
# nums.append('abc')
# print(average(30))
# print(average(40))

def make_average():
    nums = [1, 2, 3]

    def average(n):
        nums.append(n)
        return sum(nums) / len(nums)

    # 将average函数对象返回给函数
    return average


# print(make_average())#这个时候就是返回的函数内存对象二不是直接调用该函数了，且返回的是average的对象
# 首先我们要将该函数进行实例
m = make_average()
# 这个时候我们再想对num进行更改是，写上nums.append()是报错的，也就是说该闭包函数将nums对象封装了起来不让别人看见
# 从而实现一个数据的安全性,当然他也不是绝对的安全，只是在nums安全性程度上来讲；
# print(m(1))

'''
总结  ：
    函数闭包要满足三个条件
    1：函数要相互嵌套
    2：将内部函数作为返回值返回
    3：内部函数要使用到外部函数的变量
'''
