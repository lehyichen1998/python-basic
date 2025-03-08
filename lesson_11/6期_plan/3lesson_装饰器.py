'''
高阶函数：
    装饰器：
        除了闭包这种高阶函数还有我们得装饰器
        通俗的理解就是将原有的函数，添加更多的功能
        下面举几个例子
'''


# 打印一句话，那么我们定义一个函数来输出一句话
# 但是为了 这句话的美丽性 ，我来几条语句进行装饰；插入两个功能表示程序执行的前后
def say_hello():
    print('程序执行前')
    result = '你好啊~~'
    print('程序执行后')
    return result


# print(say_hello())
'''
这个时候我们发现一个问题，就是说我们要修改函数的部分十分有规律,来几个其他的函数，并添加相似功能；
这个时候就可以使用到装饰器，对函数进行装饰
'''
'''
我们可以直接修改代码，但是会有以下问题
    1如果修改过多，造成修改不方便
    2不方便后期维护，假设在后期又要对函数进行修改这个时候我们还要改代码的时候就很难维护了
    3并且这样做违反ocp原则，就是说最好是不要去动源代码（print函数举例）
我们希望在现有的函数不变的情况下，对原函数进行装饰
'''


# 例: 来个 增加的函数
def add(a, b):
    c = a + b
    return c


def new_add(a, b):
    print('程序开始')
    r = add(a, b)  # 将add实例传递给r
    print('程序结束')
    return r  # 将r值进行返回


# 我们来调用这个相加的函数
# print(new_add(1, 1))  # 这个时候我们发现函数没有值 只有程序开始，程序结束

'''
    疑问:
        经过刚才这么一波操作后，是解决了对函数装饰的问题，但是好像还是不太方便
        假设我还有个乘法要进行装饰呢？
'''

'''
    装饰器定义过程：
        外部函数接收函数名，内部函数接收对饮函数的参数
'''


def begin_end(old):  # 外部函数
    def new_fuc(a, b):  # 内部函数
        # 在new_fuc中我们写装饰器部分
        print('程序开始~~~')
        r = old(a, b)  # 我对add函数进行调用，我就要给他传参
        print('程序结束~~~')
        return r

    return new_fuc


'''
    z这个执行装饰器的部分 ，调用 两个 及以上的 函数 尽心装饰；
'''
# 来调用begin_end
# b = begin_end(add)
# print(b(1, 1),end='')

# 问题 ， 这样 装饰一个函数十分的麻烦 ，那么我们有没有办法 ，用更方便的使用 装饰器呢

'''     装饰器的 *args,**kwargs     '''


def begin_ends(old):
    '''
    我们在begin_end这层来接收外界传入old（旧的函数对象）
    里面使用*args, **kwargs进行可迭代接收，也就是说有参数我就传参数，没有参数
    我就不穿参数，这样编写装饰器大大提高了函数的核心复用率；
    '''

    def new_fuc(*args, **kwargs):
        # 在new_fuc中我们写装饰器部分
        print('程序开始~~~')
        r = old(*args, **kwargs)  # 我对add函数进行调用，我就要给他传参
        print('程序结束~~~')
        return r

    return new_fuc


'''   创建两个函数，有参和无参  '''


def say():
    return '你好'


def mult(num1, num2):
    return num2 * num1


def show_dic(dict_obj):
    return [(key,value) for key, value in dict_obj.items()]


'''  对第一个函数进行装饰   '''
# fuc = begin_ends(say)
# fuc()
'''    对第二个函数进行装饰     '''
# param_fuc = begin_end(mult)
# print(param_fuc(1, 3))
'''   对第三个函数进行装饰  '''

dc_fuc = begin_ends(show_dic)
# 创建一个字典
dc = {'name': '大雄', 'age': 25}
print(dc_fuc(dc))
