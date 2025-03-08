menu = '''
    ====通讯录管理系统====
        1.增加姓名和手机
        2.删除姓名
        3.修改手机
        4.查询所有用户
        5.根据姓名查找手机号
        6.退出
    ====================
        '''

# 认识 while 循环；
#       while 条件：（True）
# while 循环当条件满足时 ，他会一直执行；

# num1 = 10
# end = 0
# while end < num1:
#     print('测试语句')
#     end = end + 1
#     pass

# if 条件案例：
'''
num1 = 10
num2 = 20

if num1 < num2:
    print('该条件正确')
else:
    print('该条件不正确')
'''

# 定义一个容器 [] 来封装name数据
# 定义一个容器 [] 来封装phone number数据
names = ['大雄','小腹','静香']
phone_number = [123,456,789]
while True:
    # 认识input()函数；
    '''
       1: input函数的特性：
            在控台上等待用户输入，直到用户输入后，回车位置(enter)
       2: input默认接收字符串类型；
    '''
    print(menu)
    user = int(input('请输入一个序号:'))
    # print(type(a))
    # if 流程 控制语句；
    '''
    if 条件:(成立：执行if中的模块，不成立 else中代码模块)
        代码模块
    else:
        代码模块
    '''
    # 判断用户输入编号是否正确；
    if user not in [1,2,3,4,5,6]:
        print('您的输入有误，请重新输入:')
    else:
        # 如果存在 用户输入的 编号；
        if user == 1:
            # 1.增加姓名和手机
            name = input('请输入添加的用户名:')
            if name in names:
                print('已经有该用户名了，请重新添加~')
                continue  # 条过此次循环
            else:
                names.append(name)  # 添加用户的姓名；
                phone = int(input('请输入用户的手机号:'))
                phone_number.append(phone)
                # index;也是一样的
                print('用户添加成功~')
        if user == 2:
            # 2.删除姓名
            name = input('请输入你想删除用户名:')
            # 拿到用户的索引
            index = names.index(name)
            # 删除索引对应的电话；
            phone_number.pop(index)
            # 删除用户
            names.remove(name)
        if user == 3:
            # 3.修改手机号
            name = input('亲输入要修改的用户名:')
            new_phone_number = int(input('请输入新的手机号码:'))
            index = names.index(name)
            phone_number[index] = new_phone_number
            print('用户手机号完成~')
        if user == 4:
            #  4.查询所有用户
            # 第一种：
            # person = list(zip(names,phone_number))
            # for p in person:
            #     print('所有用户:',p)
            # 第二种：
            print('所有用户：')
            for p in names:
                index = names.index(p)
                phone = phone_number[index]
                print('\t\t',p,':',phone)
            pass
        if user == 5:
            # 5.根据姓名查找手机号
            name = input('请输入你查找信息的用户名:')
            index = names.index(name)
            print('您查找的手机号码为：',phone_number[index],'~')
        if user == 6:
            # 6.退出
            # 第一种；
            # print('退出通讯录管理系统~')
            # break
            # 第二种 ：
            exit()
            pass


















