'''    while      '''

'''
    三类：
        1 流程顺序：
        2 条件判断：
        3 循环语句： for   while 
        
    while  基本语法
        四步循环法：
            初始化变量
            条件判断
            循环体
            改变变量
'''
# 之前演示的 while 循环；
# while True:   # True表示恒成立
#     print('今天好i想学习')  # 死循环；

'''        四步循环法    (循环三次的效果)     '''
'''
        # 初始化变量
        num = 0
        # 条件判断
        while num < 3:
            # 循环体
            print(666)
            # 改变变量
            num = num + 1
'''

'''     10 以内的数字之和      '''
# 初始化变量 num 为 执行次数，sums 为 统计所有的数值求和；
'''
num = 1
sums = 0
# 条件判断
while num < 10:
    # 循环体内的代码；
    sums = sums + num
    # 改变变量
    num = num + 1

print(sums)
'''
'''    求100以内的 偶数合    和  奇数合     '''
'''
        100以内的偶数;
        count = 0  # 初始化变量
        sums = 0
        
        # 条件判断
        while count < 100:
            # 循环体
            if count % 2 == 0:
                sums = sums + count
            # 改变变量
            count = count + 1
        print(sums)
'''

# 直接循环过滤
'''
        count = 0
        sums = 0
        while count < 100:
            # 循环体
            sums = sums + count
            # 改变变量
            count = count + 2
        print(sums)

'''

'''         如果用户输入密码错了三次，今天不能再登录            '''

'''
    print('---请进行登陆---')
    count = 0
    while count < 3:
        password = input('请输入您的密码>>')
        if password == '123':
            print('密码正确欢迎登陆~')
            break
        else:
            print('密码错误请重新输入密码~')
        # 改变变量
        count = count + 1
'''

# 如果用户输入密码错了三次，今天不能再登录
'''
    count = 0
    while count<=3:
        count+=1
        password = input('请输入密码：')
        if password == '123':
            print('密码正确欢迎登录！')
            break
        if count==3:
            print('密码错了三次，今天不能登录')
            break

'''

''' 关于 continue  关于 break '''
# 来个 while的 五次循环；
'''
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        print('今天太快了吧~',count)
        continue
'''

# for循环中的嵌套循环；
'''
for i in range(5):  # 外层循环
    print('外外外外层循环 %d' % i)
    for j in range(5):  # 为内层循环
        print('内内内内层循环 %d' % j)
'''

# while 中的 嵌套循环；
# i = 0
# while i < 3:
#     print('外外外层循环~', i)
#     for j in range(3):
#         print('内内内内层循环', j)
#     i +=1

# 纯while 循环；
# i = 0
# while i < 3:  # 外层while循环
#     print('外外外层循环~', i)
#     j = 0
#     while j < 3:  # 内层while循环
#         print('内内内内层循环',j)
#     j += 1
#     i += 1

# 利用 while 那字典数据

# 创建字典
dc = {'name': '大雄', 'age': 60, 'hobby': 'sleep'}

# for i in dc:
#     print(i,':',dc[i],end='   ')
count = 0
# a = len(list(dc.keys()))  # len函数的作用；

# while count < len(list(dc.keys())):
#     # 打印字典的key
#     key = list(dc.keys())[count]
#     # 取value 值；
#     value = dc[key]
#     print(key, ':', value, end='')
#     count += 1


# 使用while 来取列表的值；
language = ['java','python','c','html','sql',]
# 初始化变量
counts = 0
while counts < len(language):
    value = language[counts]
    print(value,end=' : ')
    counts +=1