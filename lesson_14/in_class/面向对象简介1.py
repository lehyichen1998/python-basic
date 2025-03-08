strs = 'www.baidu.com/static/img/666.jpg'

a = 1
b = str(a)


# print(str(a))

# class chifan(object):
#     def dinner(self):
#         pass
#
#     def breakfast(self):
#         pass
#
#     pass


class Person:
    name = '大雄'
    age = '60'
    height = '160'

    def eat(self):
        return '%s正在吃饭' % self.name

    def say_hello(self):
        return '%s在向你问好' % self.name

    def sleep(self):
        return '%s正在睡觉' % self.name


p = Person()
print(p.eat())
print(p.say_hello())
print(p.sleep())
