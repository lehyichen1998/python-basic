class Person(object):
    '''init特殊: 自动执行'''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_age(self):
        return '%s的年龄为%s' % (self.name, self.age)

    def say_hello(self):
        return '%s在向你问好' % self.name

    def sleep(self):
        return '%s正在睡觉' % self.name


p = Person('大雄',60,'male')
print(p.say_hello())
