'''
for 循环 ：
    python:
    流程控制语句； if；
    循环语句； for ： while
for (基本语法)：
    for 可迭代变量 in 循环对象:

        ( iterable)可迭代变量 : 范围小；局限于 循环对象中的内容；
            案例一:
            # i的值不断在变动，随循环对象而变动；
            for i in range(5):
                print(i)
        循环对象： 可以是列表 ，也可使range函数，还可以是 字符串数据；也可以是 元组 ，字典 ；
            案例1：
                for i in ['1','2','3','4','5']:
                    print(i)
            案例2：

'''
# range 函数对象：
# for i in range(1,11,3):  # 1  2  3  4  5  6  7  8  9  10
#     print(i)
# range(起始值，终止值，跳转值)
# print(range(10))
'''
#1;练习题：
    1;100以内的数字之和
    2;100以内所有的奇数之和
    3;100以内所有的偶数和
    4;100以内5的所有倍数之和
'''
# result 用来 保存每次叠加的数据；
# debug： 调试程序，那个地方出现了错误；也可以查看程序是如何运行的；
'''     100     以内的数字之和'''
# result = 0
# for i in range(100):
#     result = result + i
# print(result)

'''     100以内的所有奇数之和    '''
# count = 0
# for i in range(1,100,2):
#     count = count +i
# print(count)

# 第二种方式；
# count = 0
# for k in range(100):
#     if k%2 == 1:
#         count = count + k
# print(count)

'''    100以内所有的偶数和      '''
# result = 0
# for j in range(0,100,2):
#     result = result + j
#     print(result)

'''    100以内5的所有倍数之和     '''
# result = 0
# for i in range(0,100,5):
#     result = result + i
# print(result)

'''     通配符     '''
# a = 1  # %d
# b = 2.111   # %.2f
# c = 'hello'  # %s
# print('我今天%s好开心'%c)

'''    1000 以内的 水仙花 数     '''
'''水仙花数是三位数起步'''
a = 987   # 9 百位 ， 8 十位  ，7 表示个位
          # 百位**3 + 十位**3  + 个位的**3 = 原来的这个数 ；
          # 1**3 + 5**3  + 3**3 = 153 ；就构成水仙数；

# num = 123
# bai = num // 100
# # print(bai)
#
# shi = num // 10 % 10
# # print(shi)
#
# ge = num % 10
# # print(ge)

for i in range(100,1000):
    # 拿出百位 ，十位 ，个位 他们的数值；
    bai = i // 100
    shi = i // 10 % 10
    ge = i % 10
    if (bai**3 + shi**3 + ge**3) == i:
        print('当前水仙花数为:',i)


