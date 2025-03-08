class Animal(object):
    def run(self):
        print('动物在奔跑!!!')

    def eat(self):
        print('动物在吃饭!!!')

    def sleep(self):
        print('动物在睡觉!!!')


class Dog(Animal):
    pass


d = Dog()
d.run()
