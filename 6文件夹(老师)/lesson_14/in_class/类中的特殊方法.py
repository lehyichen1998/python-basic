# 特殊方法
#

class Person(object):    # object 是所有类的父类
    # name = '大雄'
    '''init特性：当类对象被调用的时候自动执行'''
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        # print('我来自person类中的init特殊方法~')
    def say_hello(self):
        return '%s正在向你问好' % self.name
    def sleep(self):
        return '%s 正在睡觉' % self.name
    def say_age(self):
        return '%s 的 年龄为 %s' % (self.name,self.age)
    def jisuan(self):
        result = 1+1
        return '%s 正在计算 得出的结果为 : %d ' % (self.name,result)

p = Person('小夫',60,'male')
# print(p.say_hello())
p.name ='胖虎'
print(p.jisuan())
