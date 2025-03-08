#  1：人机 猜拳；
import random

# 1 表示 石头 ； 2表示 剪刀 ； 3 表示 布；

while True:
    cp = random.randint(1, 3)
    print(cp)
    user = input('请输入你想出的内容 ，石头 ，剪刀 ，布(继续请输入，退出按break):')
    if user == '石头' and user != None:
        user = 1
        if user == cp:
            print('平局')
        elif (user == 1 and cp == 2) or (user == 2 and cp == 3) or (user == 3 and cp == 1):
            print('玩家胜利~')

        else:
            print('电脑胜利~')
    elif user == 'break':
        print('欢迎下次来玩~')
        break
    elif user == '剪刀':
        user = 2
        if user == cp:
            print('平局')
        elif (user == 1 and cp == 2) or (user == 2 and cp == 3) or (user == 3 and cp == 1):
            print('玩家胜利~')
        else:
            print('电脑胜利')
    elif user == '布':
        user = 3
        if user == cp:
            print('平局')
        elif (user == 1 and cp == 2) or (user == 2 and cp == 3) or (user == 3 and cp == 1):
            print('玩家胜利~')
        else:
            print('电脑胜利~')
    else:
        print('请输入你的内容哦~')
