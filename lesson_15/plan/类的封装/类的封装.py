'''
刚才我们说了类的初始化
类的封装：
    那我们拿不到他们的值
        那如果我们想拿到他们的值，又想保证数据的安全
        那么这时我们需要给一个类来提供一个getter 和setter方法
    类中的setter getter方法
        getter 获取的属性
        setter 设置类中的属性
'''


class Dog():
    '''标识狗类'''

    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age
    def getter_name(self):
        return self.__name
    def setter_age(self,age):
        if age < 0:
            return '请输入正确的年龄'

    def dog_voice(self):
        return '%s正在叫~~ing' % self.__name

    def dog_color(self):
        return '%s正再土里打滚~~'

    def dog_age(self):
        return '%s狗今年%s岁了' % (self.__name, self.__age)


d = Dog('小白', '白色', 10)

d.__name = '小黑'
print(d.dog_age())

'''创建getter和setter方法'''


class Dog():
    '''标识狗类'''

    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    def dog_voice(self):
        return '%s正在叫~~ing' % self.__name

    '''定义getter方法获取__name'''

    def getter_name(self):
        return self.__name

    '''定义setter_name'''

    def setter_name(self, name):
        self.__name = name

    def getter_color(self):
        return self.__color

    def setter_color(self, color):
        self.__color = color

    def dog_color(self):
        return '%s正再土里打滚~~'

    def getter_age(self):
        return self.__age
    '''为什么会有getter  和 setter 呢，就是应为我们
    将 属性以方法的形式进行定义，这个时候我们就可以定义
    实例属性的规则，比如说你要修改的狗狗的年龄，
    那必须要满足大于0否则我提示   修改年龄不能小于10
    这就是setter 方法的好处'''
    def setter_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            return '修改的年龄不能小于0'

    def dog_age(self):
        return '%s狗今年%s岁了' % (self.__name, self.__age)


d = Dog('小白', '白色', 10)

# d.setter_name('小灰')
# print(d.getter_name())
# # print(d.dog_voice())

'''确实是可以改动里面的实例属性'''

# d = Dog('小白','白色',10)
# d.setter_name('小灰')
# print(d.setter_age(20))
# print(d.dog_age())
# print(d.getter_name())
# print(d.dog_voice())

'''
总结：
    封装的作用是什么？
    我们可以通过在类中定义好，封装好的方法来处理我要处理的数据，
    使得调用起来容易，变动起来麻烦，
    类最终的作用就是将程序简单化；
'''
