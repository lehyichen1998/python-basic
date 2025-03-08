name = []
number = []
a = '''
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
while True:
    # 首先获取用户输入
    b = input(a)
    if b not in ("1", "2", "3", "4", "5", "6"):
        input("输入有误请重新输入")
    # 判断用户是否输入的序号：
    else:
        # 如果存在
        if b == ("1"):  # 添加用户
            name1 = str(input("请输入姓名"))
            if name1 in name:
                print("已有此联系人请重新输入")
                continue
            else:
                name.append(name1)
                number1 = str(input("请输入手机号"))
                number.append(number1)
                print("输入完成")
        elif b == ("2"):  # 删除用户
            name1 = str(input("请输入要删除的联系人"))
            c = name.index(name1)
            name.remove(name1)
            del number[c]
            print("")
        elif b == ("3"):  # 修改用户
            name1 = str(input("请输入要修改的联系人"))
            c = name.index(name1)
            d = str(input("要修改的手机号"))
            number[c] = d
            print("修改完成")
        elif b == ("4"):  # 查找用户
            for i in name:
                print("所有用户有", i)
        elif b == ("5"):  # 修改手机号
            name1 = str(input("请输入您要查找的联系人"))
            c = name.index(name1)
            print("您要查找的手机号是", number[c])
        elif b == ("6"):
            print("感谢使用")
            break
        else:
            print("输入有误请重新输入")
