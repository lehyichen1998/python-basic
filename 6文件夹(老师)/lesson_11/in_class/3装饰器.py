'''

什么是装饰器呢?
    ’装饰的作用‘
    为一个普通的函数 添加更多的功能；
'''

# 案例一
'''
    其他功能 ：
        第一个功能:  ‘程序执行前’
        第二个功能:  ‘程序执行后’
'''

def say_hello():
    return 'hello'


def say_ok():
    return 'ok~'


# print(say_hello())
# print(say_ok())

'''
添加的功能是单一的，面向的函数是不单一；
我们可以修改原函数代码：
    1：如果修改过多，修改不方便；
    2: 不方便后期维护，还会影响使用该函数的函数，还会造成维护困难;
    3:  ocp原则：内层的源代码；
'''

'''    装饰器     '''
# 装饰器函数；
def begin(old_fuction): # 外部函数  ;old_fuction为装饰器装饰的函数对象；
    def end(num1,num2): # 内部函数
        print('程序开始~~~~')
        result = old_fuction(num1,num2)
        print('程序结束~~~~')
        return result
    return end

# 对say_goodbye函数进行装饰;
# fuc = begin(say_goodbye)
# print(fuc())

'''     带参装饰器    '''
def add(num1,num2):
    return num2 + num1
'''     无参函数      '''
def say_goodbye():
    return 'byebye~'
# 调用 装饰器函数装饰 add
# fuc = begin(add)
# print(fuc(1,2))


'''   装饰器的 *args,**kwargs     '''
# 完整版的 装饰器定义
def begin_end(old_fuc):
    '''
    对其他的函数进行装饰，
    *args,**kwargs ,*args表示 接受可迭代参数 **kwargs是接受字典类型的数据
    两者皆表示可有可无，有的话就接收，没有的话就不接收；
    :param old_fuc:
    :return:
    '''
    def inner(*args,**kwargs):
        # 对要装饰的函数尽心装饰
        print('程序执行前~~~')
        result = old_fuc(*args,**kwargs)
        print('程序执行后~~~')
        return result
    return inner

''' 无参    '''

def say_goodnight():
    return 'goodnight'

''' 有参  '''
def mult(num1 ,num2):
    return  num2 * num1

''' 字典类型的参数 '''
def show_dic(dic_obj):
    return [(key,value) for key,value in dic_obj.items()]


#1
# r = begin_end(say_goodnight)
# print(r())

# 2
# r = begin_end(mult)
# print(r(2, 3))

# 3
# dc = {'name':'大雄','age':60}
# r = begin_end(show_dic)
# print(r(dc))

#另外的装饰方式
@begin_end
def say():
    a = 'goodgood'
    print('程序执行前')
    print('程序执行后')
    return a

print(say())