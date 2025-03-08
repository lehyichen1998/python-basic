# 你想用的时候就用，不想用的时候就不用；


# def one():
#     print('我是第一名')
#
# # 调用该函数
# one()


# 声明一个（吃晚饭）函数:

def dinner():
    # 方法体
    print('我正在吃完饭')


# 调用函数
# dinner()

# 带参函数案例(求和函数):
# def sums(num1,num2):   # 形参:
#     result = num1 + num2
#     print(result)


# 调用函数

# sums(1,2)  # 实参：具体的某一个值；


# 认识return  :返回；
# def say_hello():
#     return '你好'
#
# print(say_hello())

# 带参 return
# def sub(num1=1,num2=3):  # 形参 默认设置成了某一个数字或者是其他的对象（str,lst......）；
#     result = num2 - num1
#     return result
#
# print(sub())

# 显示各种 str 中的数据
s = '  aa11'

for i in s:
    speace = i.isspace()  # 验证是否为 正确
    letter = i.isalpha()
    number = i.isdigit()
    print('空格:%s字母:%s数字：%s' % (speace,letter,number))

# print 函数:
