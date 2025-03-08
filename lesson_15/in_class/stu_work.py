'''


'''


class Student(object):
    def __init__(self, name=None, age=None, score=None):
        self.name = name
        self.age = age
        self.score = score

    def study(self):
        return '%s同学，通过课后不断努力取得了一个好成绩，成绩为: %s' % (self.name, self.score)

    def stu_seelp(self):
        return ''

    def run(self):
        return ''

    def input_data(self):
        lst_data = []
        while True:
            self.name = input('学生的姓名: ')
            if self.name == '':
                break
            self.age = input('学生的年龄: ')
            if self.age == '':
                break
            self.score = input('学生的成绩: ')
            if self.score == '':
                break
            stu = Student(self.name, self.age, self.score)
            lst_data.append(stu)
        return lst_data

    def show_stu(self, lst_data):
        for i in lst_data:
            print('学生姓名:%s学生年龄:%s学生成绩:%s' % (
                i.name, i.age, i.score
            ))


# s = Student('小明', 60, 100)
# print(s.study())

s = Student()

# s.show_stu(s.input_data())
lst = s.input_data()
print('lst: ', lst)
