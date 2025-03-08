'''
定义一个类
    狗类
    __init__;好处
    创建多个不一样的类对象，
'''
class Dog1():
    '''
    没有__init__
    '''
    name = '小黑'
    age = 20
    color = '黑色'
    def dog_Self(self):
        '''
        :return:返回dog的相关介绍
        '''
        print('狗狗名字叫做%s，今年%s岁了，狗狗是%s的；'%(self.name,self.age,self.color))

# 创建 Dog1的实例对象
d1 = Dog1()

# d1.dog_Self()
# 修改 Dog1 的实例属性

# d1.name = '小黄'
# d1.dog_Self()
# 直接这样去，申明是十分的不安全，也不符合规范，二期这样写死了后面的参数不好改；

# 使用__init__，特殊方法；
# 认识__init__,

class Dog2_1():
    def __init__(self):
        print('__init__方法被执行了')

# 强调 _init_会自动执行的特性；
# d2_1 = Dog2_1()
# d2_1.__init__()

class Dog2():
    '''添加Dog的实例属性'''
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def cutu(self):
        return '%s正在摇尾巴'%self.name
    def waibiao(self):
        return '%s是一只%s的狗'%(self.name,self.color)

# d = Dog2('小白','白色')
# d2 = Dog2('小黑','黑色')
# print(d.waibiao())
# print(d2.waibiao())


'''
__init__自带的影藏属性的方法
'''
class Dog3():
    '''添加Dog的实例属性'''
    def __init__(self,name,color):
        self.__name = name  #__开头的实例属性是隐藏属性
        self.__color = color
    def cutu(self):
        return '%s正在摇尾巴'%self.__name
    def waibiao(self):
        return '%s是一只%s的狗'%(self.__name,self.__color)

# d = Dog3('小白','白色')
# d2 = Dog3('小黑','黑色')
# # d.hiden_name = '小灰'
# #利用内核提供的属性方法，设置隐藏的属性名称
# d.name = '小灰'
#
# print(d.waibiao())




