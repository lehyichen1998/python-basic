'''
def say_hello():
    print('程序执行前！！！')
    print('程序执行后！！！')
    return 'hello'


def say_ok():
    return 'ok'


def say_goodbye():
    print('程序执行前！！！')
    print('程序执行后！！！')
    return 'byebye'


print(say_hello())
print(say_ok())

'''


# def say_goodbye():
#     return 'byebye'


def begin(old_function):
    def end(num1, num2):
        print('程序开始!!!')
        result = old_function(num1, num2)
        print('程序结束!!!')
        return result

    return end


# fuc = begin(say_goodbye)
# print(fuc())

def add(num1, num2):
    return num2 + num1


# fuc = begin(add)
# print(fuc(1,2))
def say_goodbye():
    return 'byebye~'


def begin_end(old_fuc):
    def inner(*args, **kwargs):
        print('程序执行前！！！')
        result = old_fuc(*args, **kwargs)
        print('程序执行后！！！')
        return result

    return inner


def say_goodnight():
    return 'goodnight'


def mult(num1, num2):
    return num1 * num2


def show_dic(dic_obj):
    return [(key, value) for key, value in dic_obj.items()]


r = begin_end(say_goodnight)
print(r())

rr = begin_end(mult)
print(rr(2, 3))

dc = {'name': '大熊', 'age': 60}
rrr = begin_end(show_dic)
print(rrr(dc))
