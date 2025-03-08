'''
class Dog:
    name = '小黑'
    age = '3'
    color = '白色'

    def dog_self(self):
        return '狗狗名字叫做%s,今年%s岁了,狗狗是%s颜色的' % (
            self.name, self.age, self.color
        )


d = Dog()
d.name = '小白'
print(d.dog_self())

d2 = Dog()
d2.name = '哆啦'
print(d2.dog_self())

d3 = Dog()
print(d3.dog_self())
'''
'''-----------------------------------------------------------------------------------------'''

'''
class Dog:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def dog_self(self):
        return '狗狗名字叫做%s,今年%s岁了,狗狗是%s的' % (
            self.__name, self.__age, self.__color
        )



d = Dog('小黑', 3, '五颜六色')
d.name = '小白'
d.__name = '小菊花'
print(d.dog_self())
'''


class Dog:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def getter_name(self):
        return self.__name

    def getter_age(self):
        return self.__age

    def getter_color(self):
        return self.__color

    def setter_name(self, name):
        self.__name = name

    def setter_age(self, age):
        if age > 0:
            self.__age = age
        else:
            return '修改的年龄不能小于零!!!'

    def setter_color(self, color):
        self.__color = color

    def dog_self(self):
        return '狗狗名字叫做%s,今年%s岁了,狗狗是%s的' % (
            self.__name, self.__age, self.__color
        )

    def dog_bark(self):
        pass


d = Dog('小黑', 99, '黑色')
print(d.getter_name(), d.getter_age(), d.getter_color())
print(d.dog_self())

print(d.setter_age(-10))
print(d.dog_self())
