names = ["大熊", "小夫", "静香"]
phone_num = [123, 456, 789]
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
exitWhile= True
while exitWhile:
    print(menu)
    user = int(input("请输入一个序号: "))
    if user not in [1, 2, 3, 4, 5, 6]:
        print("Please Enter 1 to 6...")
    else:
        if user == 1:
            print("*******1.增加姓名和手机*******")
            name = input("请输入添加的用户名: ")
            if name in names:
                print("已经有该用户名了，请重新添加")
                continue
            else:
                names.append(name)
                phones = int(input("请输入用户的手机号: "))
                phone_num.append(phones)
        elif user == 2:
            print("*******2.删除姓名*******")
            name = input("请输入你想删除的用户名: ")
            if name in names:
                index = name.index(name)
                phone_num.pop(index)
                names.remove(name)
                print(name, " 已删除!!!")
            else:
                print("请输入正确的手机号!!!")
        elif user == 3:
            print("*******3.修改手机*******")
            name = input("请输入需要修改的用户名: ")
            new_phone_num = int(input("请输入新的手机号: "))
            index = names.index(name)
            phone_num[index] = new_phone_num
            print(name, "手机号已更改至", new_phone_num)
        elif user == 4:
            print("*******4.查询所有用户*******")
            # person = list(zip(names, phone_num))
            # for p in person:
            #     print(p)

            print("所以用户: ")
            for p in names:
                index = names.index(p)
                phones = phone_num[index]
                print("\t\t\t", p, ": ", phones)
        elif user == 5:
            print("*******5.根据姓名查找手机号*******")
            name = input("请输入您要查找信息的用户名: ")
            index = names.index(name)
            print("您查找的手机号: ", phone_num[index])
        elif user == 6:
            # print("*******6.退出*******")
            # break
            # exit()
            exitWhile = False
    input("按键继续.................................")
    pass
