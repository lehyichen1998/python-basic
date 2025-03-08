'''  for 循环   '''
'''
for 循环，这个for 不同于 whlie的是 他的可迭代变量直接声明在了他的循环语句中
我们不需要额外的去声明 他的一个可迭代变量 而且他的一个作用域也会更广；列子
1；
for 可迭代变量 in 循环对象(range函数/其他变量):
    循环体；
2：嵌套循环；
    for 可迭代变量 in range函数/其他变量:（外层循环）
        for 可迭代变量 in range函数/其他变量:(内层循环)
#外层决定内层循环的循环次数，也就是说当外层循循环一次
对应的内层循环的全部执行一遍，那么我有多少的外层循环
我就执行多少内层循环    
'''
# 爬虫: 页面文字对象；
# for i in range(6):
#     print('for循环',i)

# 初始化变量
# i = 0
# # 循环条件
# while i < 6:
#     # 循环体
#     print('while循环',i)
#     for k in range(6):
#         print(6666)
#     # 改变原有的变量
#     i += 1



















# 实现99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1 ):
#         print('%d*%d=%d' % (i, j, i * j), end=' ')
#     print()

'''  while 循环   '''
'''
while 条件也称之为 条件判断表达式
    举个 if的例子  看看if 和 whlie之间的区别：
    首先：
        只要是涉及到条件的语句就会涉及bool类型
        如果条件成立，则执行里面的代码块
        否则不执行
    2：debug
whlie：四部循环法
    初始化变量
    条件判断
    循环体
    改变变量
'''
# 99 乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(i,'*',j,'=',i*j,sep='',end=' ')
        j +=1
    print()
    i += 1
