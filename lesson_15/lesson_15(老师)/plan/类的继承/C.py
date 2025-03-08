'''
类的重写：
    就是在原有的类上里面有一样的方法，但是原有的方法不满足我现在的需求
    所以我们在现有的类中，定义了一模一样的方法，就叫做重写

    在这个重写的内容中，强调重写的，方法是从哪里获取的；
    他们的列队取值顺序；
'''
from lesson_10object_下.plan.类的继承.B import Dog

class Hashiqi(Dog):
    def fansha(self):  #这就是重写，在原有的方法上进行改动
        return '哈士奇正在犯傻~~'
    def cahjia(self):
        return '哈士奇正在拆家~~ing'

h = Hashiqi()
print(h.fansha())



