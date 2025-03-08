'''
python 基本数据类型； 和 变量
    整数：
    int()  : 类；
        1,2,3,4,--无限
        -1,-20,-100
    浮点数：
    float() : 类；
        1.1 , 1.1212；
        -1.1, -1.2151654564
    字符串:
    str() : 类
        '10'  ，任何用引号引起来的字节，都是字符串；
        "10"  ,这也是一个字符串；
        'asgdhasgdkasjhasdasdasddjas' ,这也是一个字符串；
        '你好啊' ，,这也是一个字符串；
        json:
            json 是一种特殊的字符串；
            json：json字符串具有描述性；且json是独立的一种数据类型；
            json_str = '{'name':'大雄','age':'100','introduce':'大雄是来自多啦A梦里面的人物' }'
    boolean:
        True,False;
        判断一个结果是否正确； True  ，False；
        bool 他可以对其他的数据类型进行判断；

    列表：
    list():数组；
        l = []
        我们将 list看成一个容器 ,容器的大小是没有限制的，你想放什么东西就可以放什么东西；
        列表中的 各式各样的数据类型称之为 ’元素‘ ， 元素与元素之间 是用逗号隔开；
        [ 1 , 1.1 ,'strsadassdasd', () , [] , {} ]
    元组：
        tuple(): 元组；
        t = ()
        我们将 tuple看成一个容器 ,容器的大小是没有限制的，你想放什么东西就可以放什么东西；
        列表中的 各式各样的数据类型称之为 ’元素‘ ， 元素与元素之间 是用逗号隔开；
        ( 1 , 1.1 ,'strsadassdasd', () , [] , {} )
    字典：
    dict()：字典类型；
        dc = {}
        dict_str = {'name':'大雄','age':'100','introduce':'大雄是来自多啦A梦里面的人物' }

    python 中常用字符；
    '/','*','**','-','+','%','//',
'''
# 整数 int()
# num = '10'       # int,1   str 2   float3

# int() 他只能强制转换 全部是数字的 值；
# print(type(int(num)))

# 字符串 str()
# num = 10
# print(type(str(num)))

# 浮点数 float()
# num = 10
# print(type(float(num)))
# print(float(num))

# bool 类型的案例；
# a = 10 < 0
# print(a)

# ；列表类型 list
l = []
# print(type(l))

# tuple 元组类型
t = ()
# print(type(t))

# 字典类型
# dc = {}
# print(type(dc))

# bool 类型
# num = 12132
# strs = '0'
# lst = [12132,'0',{}]
# dc = {'name':"大雄"}

# print(bool(dc))  # True 2 ,False 1

'''
什么是对象：
   因为在python中 一切皆为对象； 
   概念：
   不同的数据类型，就会创建出不同对象
   列表对象
   字典对象
   字符串对象
   
'''
strs = 'https://www.baidu.com/file/img/666.jpg'
# lst = []
# dc = {}

# 对象案例：
# img = strs.split('/')[-1]
# print(img)
# lst
# dc.

'''
python 中常用运算符；
    '/','*','**','-','+','%','//',
    + :他如果 遇到整数 会让两数相加 
        如果遇到对象是字符串 他是起链接作用
    //:强除 ：他只保留 得到的整数部分；
    % :求余数
'''
# python 中常用字符 案例：
num1 = 100
num2 = 33
# 幂运算案例
# result = num1 ** num2  # 幂  100*100*100
# print(result)

# 减法案例
# result = num1 - num2
# print(result)

# 加法案例：
# result = num1 + num2  # num1num2
# print(result)

# % 求余数：
# result = num2 % num1
# print(result)

# //整除；
# result = num1 // num2
# print(result)

# 除法案例；
# result = num1 / num2
# print(type(result))

'''
变量部分：
    普通变量和可迭代变量；
    
'''
# 普通变量（variable）：
# a = 1,  # 就是一个变量；
# 普通变量中的多变量赋值；
# a = b = c = 1
# print(a,b,c)

# 可迭代变量；
# for i in range(10):
#     # 这里的i 为 可迭代变量 ，变量在根据后方 数值而不断变动；
#     print(i,end=' ')   # 1,1     i = 10 ,2   发自己答案；

# 认识逻辑判断符；
# in , ont in
# 来定义一个列表容器；
lst = [1,2,3,4,5,6,7,8,9]
x = 1000
y = 6
print(x not in lst)  # True 1  False 2




'''
作业：
    一：理解上课演示的案例；
    二：分别使用 python中 各种运算符 计算一组数值（要求使用不同的运算符，至少7个）；
    三：提取字符串 s = 'https:www.baidu.com/file/img/1024.img' 中的 1024.img
'''







