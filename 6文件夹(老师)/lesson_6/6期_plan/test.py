count = 0
while count < 3:
    user = input('请输入密码：')
    if user == '123':
        print('登录成功')
        break
    else:
        print('密码错误')
        count += 1
        if count == 3:
            print('三次出错退出系统')
            break