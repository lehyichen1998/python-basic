'''
# num = 11
# print(num > 10)
# if num > 10:
#     print('当前num大于10~')
# elif num > 20:
#     print('当前num大于20~')
# elif num > 30:
#     print('当前num大于30~')
# elif num > 40:
#     print('当前num大于40~')
# else:
#     print('num是小于10~')
'''

'''
concent = '123'
password = '321'
while True:
    user_cont = input('请输入您的账号:')
    user_pass = input('请输入您的密码:')

    if user_cont == concent and user_pass == password:
        print('登录成功!!!!!!!!!')
    else:
        print('登陆失败!!!!!!!!!')
'''

'''
while True:
    lst = ['大熊', '哆啦A梦', '静香', '胖虎']
    user = input('请输入哆啦A梦的人物:')
    if user == 'break':
        break
    if user not in lst:
        print('您输入的任务信息%s不在当前的动画片中' % user)
    else:
        print('您输入的%s是哆啦A梦中的人物' % user)
'''

'''
while True:
    user_num = int(input('请输入一个数字:'))
    if user_num % 2 == 1:
        print('您输入的数字%d为奇数' % user_num)
    elif user_num % 2 == 0:
        print('您输入的数字%d为偶数' % user_num)
'''

'''
while True:
    year = int(input('请输入年份: '))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) or (year / 3200 == 0 and year / 172800 == 0):
        print(year, '为闰年')
    else:
        print(year, '不为闰年')
'''

'''
score = int(input('请输入小明的成绩: '))
if score < 0:
    print('成绩不能为负数！！！！请输入正确成绩！！！！')
else:
    if 60 <= score < 85:
        print('下次努力~')
    elif 85 <= score < 99:
        print('奖励RM100~')
    elif 0 <= score < 60:
        print('奖励试卷一套')
    else:
        print('奖励旅游~')
'''

'''
while True:
    dog_age = int(input('请输入狗狗的年龄: '))
    like_people_age = 0
    if dog_age < 0:
        print('您输入的狗狗年龄不合法!!!')
    else:
        if dog_age <= 1:
            like_people_age = dog_age * 14
        else:
            like_people_age = dog_age * 7 + 7
    print('狗狗相比较人的年龄为%d' % like_people_age)
'''

'''
dc = {}
while True:
    key = input('请输入字典的key值,break 停止 键值插入: ')
    if key.lower() == 'break':
        print('退出插入!!!')
        break
    else:
        if key != '':
            value = input('请输入%s的value值: ' % key)
            dc.setdefault(key, value)
        else:
            print('请重新输入字典的key值!')
    print('您刚才创建的字典为', dc)
'''

'''
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(i, ' X ', j, ' = ', i * j, end='\t')
        j = j + 1
    print()
    i += 1
