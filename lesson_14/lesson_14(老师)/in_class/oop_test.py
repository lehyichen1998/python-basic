class Person:
    '''
    将类看成一个很大的容器:
    可以放置很多很多函数 (方法metohd)
    函数方法没有限制
    将方法的功能封装起来
    当有需要的时候才进行调用；
    '''
    '''
    我们平时 叫的变量在 类中 就叫做属性
    平时所说的函数 在；类中 就叫做 方法 :method
    self : 表示本身
    '''
    name = '大雄'
    age = '60'
    hight = '160'
    def eat(self):
        return '%s正在吃饭' % self.name
    def say_hello(self):
        return '%s在向你问好' % self.name
    def sleep(self):
        return '%s正在睡觉' % self.name