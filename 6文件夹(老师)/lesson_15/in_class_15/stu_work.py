# 类的练习：
"""     定义一个学生类，模拟学生，要求有基本的属性，还有学生会有的方法；        """

class Student(object):
    # 定义学生类的基本属性
    def __init__(self,name=None,age=None,score=None):
        self.name = name
        self.age = age
        self.scroe = score
    def study(self):
        # 方法体：执行的代码
        return '%s同学,通过课后不断努力取得了一个好成绩，成绩为:%s' % (self.name,self.scroe)
    def stu_sleep(self):
        return ''
    def run(self):
        return ''
    # 定义当前类接收数据的方法；
    def input_data(self):
        # 有可能接受很多的数据
        lst_data = []
        while True:
            self.name = input('学生的姓名:')
            if self.name == '':
                break
            self.age = input('学生的年龄:')
            if self.age == '':
                break
            self.scroe = input('学生的成绩:')
            if self.scroe == '':
                break
            stu = Student(self.name,self.age,self.scroe)
            lst_data.append(stu)
        return lst_data
    # 定义一个输出数据的方法:
    def show_stu(self,lst_data):
        for i in lst_data:
            print('学生姓名:%s学生年龄:%s学生成绩:%s' % (
                i.name,i.age,i.scroe
            ))



# s = Student('小明',60,100)
# print(s.study())

# 调用当前方法:
s = Student()

# 插入学生的基本数据
lst = s.input_data()
print('lst:',lst)
# 显示学生信息
s.show_stu(lst)



