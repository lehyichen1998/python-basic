'''
新建一个类，使用继承的方式来直接获取到之前的类方法；
强调一下导包；
类的继承：
    获得父类中多有的方法

'''
from 基础课程.lesson_15.plan.类的继承.A import Animal

class Dog(Animal):  #在括号中通过继承的方式拿到之前的所有的方法；
    def dog_voive(self):
        return '狗正在叫~~ing'
    def fansha(self):
        return '狗狗在犯傻~~'
d = Dog()
# print(d.eat())
# print(d.sleep())
# print(d.run())
# print(d.dog_voive())
print(d.fansha())


