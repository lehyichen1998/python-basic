'''
====通讯录管理系统====
1.增加姓名和手机
2.删除姓名
3.修改手机
4.查询所有用户
5.根据姓名查找手机号
16.退出
=====================
请选择：
'''

name = []
phone = []

massage = '''
            ====通讯录管理系统====
            1.增加姓名和手机
            2.删除姓名
            3.修改手机
            4.查询所有用户
            5.根据姓名查找手机号
            16.退出
            =====================
          '''
while True:
    print(massage)
    user = int(input('请选择你要执行的序号>>>'))
    # 判断用户的序号
    if user in [1, 2, 3, 4, 5, 6]:
        if user == 1:  # 1.增加姓名和手机
            username = input('请输入要添加的用户姓名：')
            if user in name:
                print('用户名重复！')
                continue
            else:
                name.append(username)
                userphone = input('请输入用户电话：')
                phone.append(userphone)
                print('添加成功！！')
        elif user == 2:  # 2.删除用户
            username = input('请输入要删除的用户名：')
            if username in name:
                username_index = name.index(username)  # 返回用户的索引
                name.remove(username)  # 删除name列表里面的用户名
                phone.pop(username_index)  # 删除电话列表的里面的电话
                print('删除成功！！')
            else:
                print('用户不存在！！')
        elif user == 3:  # 3.修改手机号
            username = input('请输入要修改手机号的用户名：')
            username_index = name.index(username)
            new_phone = input('请输入用户的新手机号：')
            phone[username_index] = new_phone
            print('修改成功！！')
        elif user == 4:  # 4.查询所有用户
            for i in name:
                print(i, end='')
        elif user == 5:  # 5.根据姓名查找手机号
            username = input('请输入用户名：')
            username_index = name.index(username)
            print(phone[username_index])
        elif user == 6:  # 16.退出
            print('欢迎下次使用哦~~')
            break
    else:
        print('您的输入有误')
