'''    函数部分      '''

# 1：利用函数对大量的的数据进行求和
# def sums(*num):#形参
#     result =0
#     for i in num:
#         result+=i
#     return result
#
# print(sums(*[i for i in range(5)]))

# 判断  一个数是否大于 5
# def func(l):
#     # return True if len(l) > 5 else False
#     return len(l) > 5 #比较运算本身返回bool值
# num = input('亲输入一个数值')
# print(func(num))#结果：True

'''    返回最大的数    '''
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

'''     拿到最高成绩      '''


# def get_max_socre(score_dic):
#     """
#     返回学生考试成绩的最高分的科目和分数
#     :param score_dic:
#     :return:
#     """
#     max_score = 0  # 封装成绩
#     max_score_course = ''  # 封装科目名
#     for course, score in score_dic.items():  # items 是字典里的实例方法
#         if score > max_score:  # 循环取值判断，拿到最大的数值
#             max_score = score
#             max_score_course = course
#
#     return max_score_course, max_score  # 将结果返回给该函数

# 创建一个字典；
# dic = {
#     '语文': 90,
#     '数学': 97,
#     '英语': 98
# }
#
# for i, s in dic.items():
#     # print('科目:%s 成绩:%d' % (i, s))
#     pass
# course, score = get_max_socre(dic)
# print(course, score)
# print(get_max_socre(dic))


'''       认识递归函数           '''
# 递归函数是一种特殊的函数，函数内部会调用函数自身,
"""
计算number的阶乘
:param number:
:return:
例如: 5 : 5 * 4 * 3 * 2 * 1
"""
# def recursion(number):
#
#     if number == 1:
#         return 1
#     next_recursion = recursion(number-1)
#     return (next_recursion * number)
# print(recursion(5))


