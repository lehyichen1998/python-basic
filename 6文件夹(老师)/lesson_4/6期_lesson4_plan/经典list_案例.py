'''                #利用列表实现敏感词汇的屏蔽         '''


# li = ['憨憨', '笨蛋']
# while True:
#     user = input('请输入一句话，enter退出>>>')
#     for i in li:
#         if i in user:
#             # 将***替换当前 user对象 中 和列表中 相等的 字符串；
#             print('***'.join(user.split(i)))
#     if user == '':
#         break


'''                 #字符串去重           '''

drinks = ['cola','rm5','tin','cold','cola']
new_drinks = []
for name in drinks:
    if name not in new_drinks:
        new_drinks.append(name)
print(new_drinks)


