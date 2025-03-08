'''
在类的概念中我们可以定义变量以及函数
    -变量在该类中会称为公共属性，所有的属性实例都可以通过类.对象来访问到
    -函数在类中称为公共方法,所有的公共方法都可以通过类的实例对象.方法名()来访问到
  注意：
    所有类中的方法在调用时，都会传递一个类的默认参数，这个参数在3.6的版本之后，会自动创建
    虽然不需要写，但是我们要知道我们在传递参数的时候还是要知道他第一个传递的参数是默认参数
    默认参数是self；

类class概念：
    - 我们目前所学的内容都是python的内置对象
    - python内置对象可以满足我们日常需求
    但是满足不了真正意义上的开发需求，应为开发需求是需要
    根据市场的变动而变动的，也就是说我们要根据实际
    情况来编写我们的代码，拿‘吃饭’来说python里面就没有
    吃饭的类，但是我们日常生活中就有吃饭个事情；
    - 其实我们学了很多的python内置类
    str(),int(),list(),bool()#都是小写字母开头
    - 所以我们在定义类的时候要使用大写来定义我们自自己创建的类，便于区分

来创建类：
     -类是对实际生活中的一个抽象，来模拟真实生活
     -归纳；所有的事物基本由亮点构成
        -特征(数据:类属性的实例  name ）
        -行为(方法：函数  )

定义一个类：
    模拟现实生活中的存在的事例；

'''
#我们来定义一个人类
    #我们在定义人类的时候我么要知道我们要做什么，定义人类的目的是什么
    # -特征(数据:类属性的实例  name ）
    # -行为(方法：函数  )

class Person:
    #人数常有的数据
    name = '胖虎'     #name是实例公共属性
    age = 20
    gender = 'man'
    #行为，方法
    def say_hello(self):
        return '%s说了声hello~'%self.name
    def say_age(self):
        return '年龄为%s'%self.age
    def say_gender(self):
        return '性别为%s'%self.gender

p = Person()      #p称之为实例对象
print(p.say_hello())
# print(p.say_age())
# print(p.say_gender())
# #这样声明不安全
# p2 = Person()
# p2.name = '小夫' #对Person的实例对象 p2进行更改
# print(p2.say_hello())

#为了避免这种现象产生，规划我们整体的代码
#使用__init__特殊方法

class Person:
    #人数常有的数据
    # name = '胖虎'     #name是实例属性
    # age = 20
    # gender = 'man'
    #使用init方法
    '''
    来定义我们特殊方法的属性，要求使用__init__
    我们的特殊方法__init__他就是会自动调用
    self.name = name
        self.age = age
        self.gender = gender
    '''
    def __init__(self,name,age,gender):
        # print('666666')
        self.__name = name
        self.age = age
        self.gender = gender
    #行为，方法
    def say_hello(self):
        return '%s说了声hello~'%self.__name
    def say_age(self):
        return '年龄为%s'%self.age
    def say_gender(self):
        return '性别为%s'%self.gender
    def get_person_age(self):
        '''
        :param age: 用于接收一个age变量对这个变量的数值进行判别
        :return: 返回一个数据
        '''
        if self.age >= 70:
            return '老年人'
        if 30 <= self.age <= 55:
            return '中年人'
        if 15 <= self.age < 30:
            return '年轻人'
    def should_we_do(self,old_fuc):
        '''
        类中的方法封装方法
        :param old_fuc: 接收传来的老函数名
        :return: 返回一个字符串； 各年龄段该做的事
        '''
        if old_fuc == '老年人':
            return '安心养老~'
        if old_fuc == '中年人':
            return '好好工作'
        if old_fuc == '年轻人':
            return '要讲武德~'

# p1 = Person()
# p.__init__()
#创建一个新的对象
# p = Person('静香',18,'女')
# p.name = '多啦A梦'
# print(p.say_hello())
'''
特殊方法定义的好处？
    属性的值，灵活传播   
    有利于他的代码的安全性
    不容易被其他的程序员改动
'''
'''
有利于类的封装，能写很多的方法,方法中还能写方法~
'''
'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
'''

p = Person('静香',18,'女')
result = p.get_person_age()  #返回年龄特征
print(p.should_we_do(result))


'''
作业：
    用类来模拟圣后中的事情：
    调用里面的方法~；
'''