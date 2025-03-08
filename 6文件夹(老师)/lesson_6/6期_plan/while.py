'''
流程控制语句
    三类
        1流程顺序：
        2条件判断：
        3循环语句：
1:while 也是条件语句
    首先：
        只要是涉及到条件判断。bool：True，False
        如果为True，则成立
        否则不成立
2： 四步循环法：
    初始化变量
    条件判断
    循环体
    改变变量

while循环中的
    break：用于退出当前循环
    continue：不进行此次循环
'''
'''         演示死循环的存在    
    whil True
'''
'''         演示循环每次执行的过程'''
'''
#            练习：求10以内的数字之和
    # 初始化变量
    # num = 1
    # # sum这个变量是我用来保存求和数据的
    # sum = 0
    # # 条件判断
    # while num<3:
    #     # 循环体
    #     sum = sum+num
    #     # 改变变量的值
    #     num=num+1
    # print(sum)
'''

# while 3

# 初始化变量
a = 0
b = '测试的字符串'
# 条件判断
while a < 5:
    # continue的作用 ，表示跳过此次循环;
    # 当a = 2 跳过这个打印;
    if a == 1:
        a+=1
        break
    print('当前循环执行了%s 次' % b)

    a += 1



'''         #习题二
        # 求100以内的偶数和与奇数和
        # num = 0
        # sum = 0
        # while num <100:
        #     if num%2 == 0:
        #         sum=sum+num
        #     num+=1
        # print(sum)
'''
'''             关于break
        #如果用户输入密码错了三次，今天不能再登录
        # count = 0
        # while count<=3:
        #     count+=1
        #     password = input('请输入密码：')
        #     if password == '123':
        #         print('密码正确欢迎登录！')
        #         break
        #     if count==3:
        #         print('密码错了三次，今天不能登录')
        #         break
'''
'''     # continue
        # num = 0
        # while num<10:
        #     if num == 3:
        #         num= num +1
        #         break
        #     print('今天好想学习~~',num)
        #     num=num+1
'''
'''     练习：利用while 来拿列表，字典的数据
        # l = ['a','b','c']
        # print(type(len(l)))
        # a = 0
        # while a<=len(l)-1:
        #     print(l[a])
        #     a =a+1
        # s = 'java'
        # print(len(s))
'''
'''     #利用while拿字典数据

        # d = {'name':'小白','age':20,'gender':'无'}
        b = 0
        while b<len(list(d.keys())):
            key = list(d.keys())[b]
            value = d[key]
            print(key,':',value)
            b = b+1
'''
'''     #认识whlie嵌套的概念
        # i = 0
        # while i<3:
        #     print('外层循环',i)
        #     j = 0
        #     while j<3:
        #         print('内内内层循环',j)
        #         j=j+1
        #     i= i+1
'''

'''     #99乘法表：while

        i = 1
        while i<=9:
            j = 1
            while j<=i:
                print('%dx%d=%d'%(i,j,j*i),end='\t')
                # print(str(i)+'x'+str(j)+'='+str(j*i),end='\t')
                j = j+1
            print()#标识换行
            i=i+1
'''
