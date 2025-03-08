#

# li= [11,22,33,44,55,66,77,88,99,90]
# dc = {'<66':['这是封装小于66的容器'],'>66':['这是封装大于66的容器']}
# print( dc['<66'])
# for i in li:
#     if i > 66:
#         # 将dc字典对象的 value插入 对应的数值；
#         # 当前dc是一个列表对象；
#        dc['>66'].append(i)
#     else:
#         dc['<66'].append(i)
# print(dc)

'''
(1)：页面显示 序号 + 商品名称，如：(使用字典和列表)
        1 手机
        2 电脑
(2)： 用户输入选择的商品序号，然后打印商品名称
(3)：用户输入886，退出程序。
'''
# 创建原数据；
dc = {1:'手机',2:'电脑'}
# 创建 一个列表保存 用户选择的 商品信息；
user_lst = []
# 重复显示；
while True:
    print('----所有商品----')
    for i in dc:
        print(i,dc[i])
    user = int(input('请输入您想要的商品编号:'))
    # try语句中表示截取异常
    # 如果这 try语句中 代码出错 ，他不会让他报错，他会让代码继续执行 ，执行except语句中的代码；
    try:
        if user != '':
            print(dc[user])
            user_lst.append(dc[user])
    # 释放异常
    except:
        if user == 886:
            print('您所购买 的 商品为 ：%s欢迎下次选购~'%(user_lst))
            break









