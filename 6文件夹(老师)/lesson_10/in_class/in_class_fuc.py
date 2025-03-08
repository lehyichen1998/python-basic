'''  函数部分   '''

# def say_hello():
#     print('hello')

# print(1,'*',1,'=',1)

# 利用函数对大量的数据进行求和
''' 
我们会定义很多函数，sum

'''
# def sums(*lst):
#     # 声明一个变量 统计求和 数据、
#     result = 0
#     for i in lst:
#         result += i  # 1+2+3+4
#     return result
# lst = [i for i in range(5)]
# # print(lst)
# print(sums(lst))

# * 的作用
# 由单个参数编程 添加多个 参数；

'''    判断  一个数是否大于 5    '''


def more_than_five(num):
    return num > 5


# print(more_than_five(6))

'''   返回的最大数      '''


def get_max(lst):
    '''
    取最大值；
    :param lst:  表示接受 一个 列表
    :return: 最大的 数值；
    '''
    if not lst:
        return None
    # 我们假设 一个列表中 的第一个数字就是最大的
    max_num = lst[0]
    for i in lst:
        if max_num < i:
            max_num = i
    return max_num


# 定义一个生成随机数的函数列表
def random_num_lst(count):
    lst = []
    import random
    for i in range(count):
        v = random.randint(1, 100)
        lst.append(v)
    return lst


# print(random_num_lst(10))
# lst = random_num_lst(10)
# print(lst)
lst = []
# print(get_max(lst))

'''    在字典中拿最高成绩     '''

# dc = {'python': 90, 'java': 99, 'html': 50, 'sql': 66}
#
#
# def get_max_score(dc_score):
#     '''
#     用于取字典数据；
#     :param dc_score:
#     :return: 最高成绩 以及科目
#     '''
#     # 定义变量保存科目
#     max_cours = ''
#     # 定义变量保存 科目对应的成绩
#     max_cours_score = 0
#     for cour, score in dc_score.items():
#         if max_cours_score < score:
#             max_cours_score = score
#             max_cours = cour
#     return max_cours_score,max_cours
# # print(get_max_score(dc))
# cour, score = get_max_score(dc)
#
# print(score,cour)

'''   递归函数     '''


# 阶乘 ？:
# 求 5 的阶乘
# 5的阶乘 = 5*4*3*2*1 = 120 , 10000
# print(5*4*3*2*1)

# loop
# 3的阶乘 = 3*2*1
# n = 5
# for i in range(1,5):
#     n = n * i
#     # 第一次 5 = 5 * 1
#     # 第二次 10 = 5 * 2
#     # 第三次 30 = 10 * 3
#     # 第四次 120 = 30 * 4
#     # 1的阶乘 = 1 * 1 = 1
#     # 2的阶乘 = 2 * (1的阶乘) = 2
#     # 3的阶乘 = 3 * (2的阶乘) = 3 * 2的阶乘
#     # 4的阶乘 = 4 * (3的阶乘) = 4 * 3的阶乘(2的阶乘*1的阶乘)
#     # 5的阶乘 = 5 * (4的阶乘) = 5 * 4的阶乘(3的阶乘*2的阶乘*1的阶乘)
# print(n)

# 根据以上的关系 我们可以做一个阶乘递归函数函数

# 递归是类似宇哥解决问题的方式 ，和循环非常的类似
# 他会将一个问题一个一个进行拆分，直到无法分解吗，在解决；
# 一个是基线条件
# 当问题被分解成最小的条件时，递归就不存在了
# 递归条件
# 将问题继续分解的条件

# 最简单的递归定义
def factorial(num):
    # 定义基线条件
    if num == 1:
        return 1 * 1
    # 递归条件
    return num * factorial(num - 1)


print(factorial(6))
