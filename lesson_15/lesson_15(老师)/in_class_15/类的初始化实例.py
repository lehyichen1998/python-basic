'''
 第一个：
        初始化实例
        init特殊方法：__init__
        为类中的属性自动传值给类中的方法，而类中的方法在获得
        __init__中的属性时需要通过self.的形式来获得
        这样在极大程度上保证的实例属性的安全性
'''

# 定义一个狗类：

# class Dog:
#     # 狗狗基本有的属性
#     name = '小黑'
#     age = '3'
#     color = '黑色'
#     # 狗狗的基本方法
#     def dog_self(self):
#         '''
#         这是对狗狗的一个基本描述的方法,用于向别人介绍该狗狗有的基本属性；
#         :return: 字符串对象
#         '''
#         return '狗狗名字叫做%s,今年%s 岁了，狗狗是%s的' % (
#             self.name, self.age, self.color
#         )

# d = Dog()
# d.name = '小白'
# print(d.dog_self())
#
# d2 = Dog()
# d2.name = '哆啦'
# print(d2.dog_self())
#
# d3 = Dog()
# print(d3.dog_self())

# 实例属性 就固定死了，实例属性的安全性；


''' -------------------------------------------------------------------------------------------- '''
# 类的初始化实例；
'''
__init__  # object
__str__
'''
class Dog:
    # 初始化实例的自带隐藏方法；
    # 狗狗基本有的属性
    '''  __init__这个特殊方法会自动执行   '''
    def __init__(self,name,age,color):
        """
        python有个自带的隐藏方法双下划线的写法可以有效的将原属性进行隐藏
        """
        self.__name = name  # hidden 的属性
        self.__age = age
        self.__color = color
    # 狗狗的基本方法
    def dog_self(self):
        '''
        这是对狗狗的一个基本描述的方法,用于向别人介绍该狗狗有的基本属性；
        :return: 字符串对象
        '''
        return '狗狗名字叫做%s,今年%s 岁了，狗狗是%s的' % (
            self.__name, self.__age, self.__color
        )

d = Dog('小黑',3,'黑色')
d.name = '小白白'
d.__name = '小菊花'
# self.__name ='小菊花'


print(d.dog_self())



















