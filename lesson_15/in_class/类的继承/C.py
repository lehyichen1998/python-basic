from 基础课程.lesson_15.in_class.类的继承.B import Dog


class hashiqi(Dog):
    def fansha(self):
        print('哈士奇犯傻!!!')

    def chaijia(self):
        print('哈士奇正在拆家!!!')


h = hashiqi()
h.fansha()
