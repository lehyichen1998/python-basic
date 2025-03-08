# 面向对象练习:
"""侧重于面向对象"""
"""     定义一个学生类，模拟学生，要求有基本的属性，还有学生会有的方法；        """

# 例：
# 01.自己写一个Student类,此类的对象有属性name, age, score, 用来保存学生的姓名,年龄,成绩:
# 1) 写一个函数input_student读入n个学生的信息,用对象来存储这些信息(不用字典),并返回对象的列表
# 2) 写一个函数output_student 打印这些学生信息(格式不限)
class Student():
    # 定义类方法的基本属性
    def __init__(self, name=None, age=None, score=None):
        self.name = name
        self.age = age
        self.score = score

    # 定义接受数据的方法
    def input_student(self):
        L = []
        while True:
            self.name = input("姓名:")
            if not self.name:
                break
            self.age = input("年龄:")
            if not self.age:
                break
            self.score = input("成绩:")
            if not self.score:
                break
            s = Student(self.name,self.age, self.score)
            L.append(s)
        return L

    # 定义显示数据的方法；
    def output_student(self,lst):
        for i in lst:
            print("姓名:%s 年龄:%s 成绩:%s" % (i.name, i.age, i.score))



s = Student()
# 调用 输入的方法为 学生添加基本信息，并返回 列表对象
l = s.input_student()
print('l:',l)
# 显示 学生有的 东西
s.output_student(l)

