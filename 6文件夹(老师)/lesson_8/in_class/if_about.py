'''
流程控制语句
    1:顺序语句
        代码执行顺序；
    2：条件语句
        if
        elif
        else
    3：循环语句
        while
        for

    if条件语句：
    if 条件:
        当前的if模块内执行的语句
        代码吗模块：print(666)
    elif 条件:
        对应代码模块
    # elif 可以写多个；
    else:  # 否则
        # 具体情况还是要看你们要去完成一个什么功能

    if 中的条件:
    判断符号
        != :  不等于
        == : 表示等于
        < : 表示 小于
        > : 表示大于
        <= , >= : 小于等于 和 大于等于 ；
    链接符号:
        and : 两个条件都要满足 ，或者两个以上的条件都要满足；
        or  : 两个或者两个以上的条件 满足一个即可；
        in : 当前的条件对象 ， 在 in 后面的 对象中 ；
        ont in :  当前的条件对象 ，没有 在 in 后面的 对象中 ；

第二部分:
小练习：
    1编写一个程序，获取一个数字，对数字进行奇数偶数判断，
        判断条件为：%
    2编写一个程序，判断判断一个年份是否为闰年
        判断条件为可以被400整除，不能被100整除，或者可以被4整除
        判断条件为：%
    3编写一个程序，如果小明的成绩为60-85，下次努力，成绩为85-99，输出奖励现金100MR，成绩为100，
        奖励免费旅游，那么如果低于60，则奖励试卷一套；
    4编写一个程序，判断狗狗的年龄
        计算寿命的简单方法是：犬的第一年相当于人活14年，以后，犬每活一年相当于人活7年。
        也就是说，假若一只犬活到10年的话，则相当于人活到了77岁。
'''
# concent = '123'
# password = '321'
#
# # 获取用户的输入
# while True:
#     print('====登录验证====')
#     user_cont = input('请输入您的账号:')
#     user_pasw = input('请输入您的密码:')
#     # 密码判断
#     if user_cont == concent and user_pasw == password:
#         print('登录成功~')
#     else:
#         print('登录失败~')

#  in  和 not in；
# while True:
#     lst = ['大熊','哆啦A梦','静香','胖虎']
#     user = input('请输入哆啦A梦中的人物:')
#     if user == 'break':
#         break
#     if user not in lst:
#         print('您输入人物信息%s不在当前的动画片中' % user)
#     else:
#         print('您输入的%s是哆啦A梦中的人物' % user)


# 1编写一个程序，获取一个数字，对数字进行奇数偶数判断，
# while True:
#     user_num = int(input('请输入一个数字'))
#     if user_num % 2 == 1:
#         print('您输入的数字%d为奇数' % user_num)
#     elif user_num % 2 == 0:
#         print('您输入的数字 %d为 偶数' % user_num)

# 2编写一个程序，判断判断一个年份是否为闰年：

# ①、普通年能被4整除且不能被100整除的为闰年。（如2004年就是闰年，1900年不是闰年）
# ②、世纪年能被400整除的是闰年。（如2000年是闰年，1900年不是闰年）
# 对于数值很大的年份，这年如果能整除3200，并且能整除172800则是闰年。
# while True:
#     year = int(input('请输入一个年份:'))
#     # 判断闰年 ；
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) or (year % 3200 == 0 and year % 172800 == 0):
#         print(year, '为闰年')
#     else:
#         print(year, '不为闰年')

# 3编写一个程序，如果小明的成绩为60-85，下次努力，成绩为85-99，输出奖励现金100MR，成绩为100，
# 奖励免费旅游，那么如果低于60，则奖励试卷一套；

# 有 1  没 0
'''    一定要注意流程走向，语句的合法性；    '''
# while True:
#     score = int(input('请输入小明的成绩:'))
#     if score < 0:
#         print('成绩不能为负数~')
#     else:
#         if 60 <= score < 85:
#             print('下次努力~')
#         elif 85 <= score < 99:
#             print('奖励100RM~')
#         elif score < 60:
#             print('奖励试卷一套')
#         else:
#             print('奖励旅游~')

'''     4编写一个程序，判断狗狗的年龄
        计算寿命的简单方法是：犬的第一年相当于人活14年，以后，犬每活一年相当于人活7年。
        也就是说，假若一只犬活到10年的话，则相当于人活到了77岁。
'''

# while True:
#     dog_age = int(input('请输入狗狗的年龄:'))
#     like_people_age = 0
#     if dog_age < 0 :
#         print('您输入的狗狗年龄不合法')
#     else:
#         if dog_age <= 1:
#             like_people_age = dog_age * 14
#         else:
#             # dog:1, person:14  dog:2  , person:21
#             like_people_age = dog_age * 7 + 7
#     print('狗狗相比较人的年龄为 %d' %like_people_age)


'''     第三部分       '''
#  while 字典添加 案例 :利用while来向字典中不断的添加数据,直到我输入break停止；
# dc = {}
# while True:
#     key = input('请输入字典的key值,break 停止 键值插入:')
#     if key == 'break':
#         print('退出插入')
#         break
#     else:
#         if key != '':
#             value = input('请输入%s的value值' % key)
#             dc.setdefault(key, value)
#         else:
#             print('请重新输入字典的key值!')
# print('您刚才创建的字典为',dc)

#  99乘法表：（while） 案例；

# 初始化变量
# 给定条件
# 循环内容
# 改变初始化变量
# i = 1
# while i <= 9:
#     # 循环的内容为内层
#     j = 1
#     while j <= i:  # True
#         print(i, 'x', j, '=', i * j,end='   ')
#         j += 1
#     print()
#     i = i + 1

# print()

## 作业完成人机猜拳；
