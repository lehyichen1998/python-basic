'''
第二个：
     类的封装:
        1:之前讲到类的封装就是一个类中有很多方法，这是笼统的
        那么我们封装的用意是为了让数据更加安全；
        2:为什么会用到类的封装
            我们有些数据不能被恶意的篡改;\
            可以根据你的你要求进行更改
        3:类的封装：
            类中的setter getter方法
            getter 获取的属性
            setter 设置类中的属性
        getter he setter 他们核心的方法是去修改self的属性
        -使用封装的方式在一定程度上提高了类的安全性
        但是他也增加类创建的复杂程度
'''

# # 狗狗的 类
# class Dog:
#     # 初始化实例的自带隐藏方法；
#     # 狗狗基本有的属性
#     '''  __init__这个特殊方法会自动执行   '''
#     def __init__(self,name,age,color):
#         """
#         python有个自带的隐藏方法双下划线的写法可以有效的将原属性进行隐藏
#         """
#         self.__name = name  # hidden 的属性
#         self.__age = age
#         self.__color = color
#     # 狗狗的基本方法
#     def dog_self(self):
#         '''
#         这是对狗狗的一个基本描述的方法,用于向别人介绍该狗狗有的基本属性；
#         :return: 字符串对象
#         '''
#         return '狗狗名字叫做%s,今年%s 岁了，狗狗是%s的' % (
#             self.__name, self.__age, self.__color
#         )
#     def dog_bark(self):
#         pass


# d = Dog('小黑',3,'黑色')
# 我要获得他的基本属性的值
# 我还要修改他的基本属性值
print()
'''    手动创建getter  和 setter 方法     '''

# 狗狗的 类
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
    # 手动创建 getter 和 setter 方法
    def getter_name(self):
        return self.__name
    def getter_age(self):
        return self.__age
    def getter_color(self):
        return self.__color
    # setter 方法 设置属性值
    def setter_name(self,name):
        self.__name = name
    '''
        为什么会有getter  和 setter 呢，就是应为我们
        将 属性以方法(函数)的形式进行定义，这个时候我们就可以定义
        实例属性的规则（由我们来规定），比如说你要修改的狗狗的年龄，
        那必须要满足大于0否则我提示   修改年龄不能小于10
        这就是setter 方法的好处
    '''
    def setter_age(self,age):
        if age > 0:
            self.__age = age
        else:
            return '修改的年龄不能小于0'
    def setter_color(self,color):
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
    def dog_bark(self):
        pass


# 调用
d = Dog('小黑',12,'黑色')
# 获取 基本属性
# print(d.getter_name(),d.getter_age(),d.getter_color())
print(d.dog_self())

# 设置 基本属性

print(d.setter_age(-10))
print(d.dog_self())

'''
总结：
    类中的封装是什么？
        我们可以通过在类中定义和封装好的方法来处理我要处理的数据；
        使得调用起来容易，变动起来麻烦
        类封装的作用最终的目的是为了确保程序数据的安全和数据稳定
        以及的将程序模块化；
'''







