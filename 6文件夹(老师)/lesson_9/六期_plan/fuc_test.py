
a = lambda a,b :a+b


'''
1：什么是函数
    函数的作用：
        为什么会有函数的存在?
        为了提代码的复用率
        还可以封装代码,想用的时候就用,就不用了
    函数：
        封装一种方法：
        在需要该方法时再对其进行调用；
    声明一个函数：
        #声明一个函数：
            def dinner():
                print('晚上好，吃饭了没有')
2
    #调用
    函数名()

    什么是函数？
        正常情况下：叫函数
        写在class类中的函数：叫做方法
    #紫色字体的代码模块一般称为python内置函数

    函数也是以对象的形式存在的
    在python中一切皆为对象，
        def ok():
            print(666)
        print(ok)
        # 显示该函数的内存地址；
    如果给函数加上括号:
        就调用当前函数，执行这个函数的方法体
    如果我不加括号：
        就是调用函数对象
3
    带参函数
        def sum(num1,num2):   #这两个参数叫做形参,参数名称要具有描述性
            方法体(代码模块)
            写具体执行某个功能，代码

        sum(1,1)  #实参
    #函数返回值
         函数返回值，就是将函数返回给这个函数
         return  返回值

    def add(a,b):
        c= a+b
        return c


常用函数库:
    求绝对值abs(),求最大值max(),z最小值min()
    强类型的函数 int()，float(),str(),tuple(),dict(),zip(),list()
    len()

    python中常用的函数https://blog.csdn.net/lm_is_dc/article/details/80048400
'''

# print('1'+str(1))


# 定义一个求和的函数
# def sum(num1,num2):
#     sum = num1+num2
#     print(sum)

# sum(1, 1)
# sum(1, 1)
# sum(1, 1)
# sum(1, 1)
# sum(1, 1)
'''
关于内置函数以及自己定义的函数
    
'''
# 函数练习
# print(abs(-1))
# 定一个myabs()
# def myabs(a):
#     if a>=0:
#         return a
#     else:
#         return -a
# print(myabs(-1))

# a = [1,-2,69,20,40]
# print(sum(a))
# help(help)

# 函数测试
# l = input('请输入一串字符')
# def count(l):
#     strs = 0      # 统计字符串
#     ints = 0      # 统计整数类型
#     kongge = 0    # 统计空格 类型
#     for i in l:
#         if i.isdigit(): # 返回 True识别数字
#             ints +=1
#         if i.isalpha():#是被字符串
#             kongge +=1
#         if i.isspace():#判断空格
#             strs +=1
#     return strs,ints,kongge

'''     # 手动实现 取最大值   
        1:定义取最大数的函数
        2：生成数据 并显示；
  '''

# def get_max(lst):
#     """
#     返回列表lst的最大值
#     :param lst:
#     :return:
#     """
#     if not lst:
#         return None
#     max_value = lst[0]  # 假设第一个是最大的数值
#     for item in lst:
#         if item > max_value:
#             max_value = item
#
#     return max_value
#
#
# from random import randrange
# lst = [randrange(10,100) for i in range(10)]
# print(lst)
# print(max(lst))
# max_value = get_max(lst)
# print(max_value)


'''     拿到最高成绩      '''


def get_max_socre(score_dic):
    """
    返回学生考试成绩的最高分的科目和分数
    :param score_dic:
    :return:
    """
    max_score = 0  # 封装成绩
    max_score_course = ''  # 封装科目名
    for course, score in score_dic.items():  # items 是字典里的实例方法
        if score > max_score:  # 循环取值判断，拿到最大的数值
            max_score = score
            max_score_course = course

    return max_score_course, max_score  # 将结果返回给该函数

# 创建一个字典；
dic = {
    '语文': 90,
    '数学': 97,
    '英语': 98
}

for i, s in dic.items():
    # print('科目:%s 成绩:%d' % (i, s))
    pass
course, score = get_max_socre(dic)
# print(course, score)




# 递归函数是一种特殊的函数，函数内部会调用函数自身,
"""
计算number的阶乘
:param number:
:return:
例如: 5 : 5 * 4 * 3 * 2 * 1
"""
def recursion(number):

    if number == 1:
        return 1
    next_recursion = recursion(number-1)
    return (next_recursion * number)
print(recursion(5))
