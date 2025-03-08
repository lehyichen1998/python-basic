strs = 'www.baidu.com/static/img/666.jpg'

a = 1    # a 只会 有整数类型的 方法，

b = str(a)   # b接收了str(a)这个对象 ,那么 此时的b就又 字符串对象中所有的方法；

# print(type(b))

# python中的内置类
# list,tuple,str,int,float,dict,   # 主要的内之类模块对象；
# print(list)
# print(tuple)
# print(str)
# print(dict)


# 定义一个类
# 定义类的语法； class 类名():  定义一个人的类

class Person:
    '''
    将类看成一个很大的容器:
    可以放置很多很多函数 (方法metohd)
    函数方法没有限制
    将方法的功能封装起来
    当有需要的时候才进行调用；
    '''
    '''
    我们平时 叫的变量在 类中 就叫做属性
    平时所说的函数 在；类中 就叫做 方法 :method
    self : 表示本身
    '''
    name = '大雄'
    age = '60'
    hight = '160'
    def eat(self):
        return '%s正在吃饭' % self.name
    def say_hello(self):
        return '%s在向你问好' % self.name
    def sleep(self):
        return '%s正在睡觉' % self.name

# 类使用；
# p2 = Person()
# p = Person()   # p 是 Person实例对象

# print(isinstance(p2, Person))

# print(p.eat())
# print(p.say_hello())
# print(p.sleep())


# 初始化实例对象
# p = Person()
# p.name = '胖虎'
# print(p.eat())








