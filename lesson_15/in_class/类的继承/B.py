from 基础课程.lesson_15.plan.类的继承.A import Animal


class Dog(Animal):
    def dog_bark(self):
        print('狗在叫!!')

    def fansha(self):
        print('狗狗正在摇尾巴~!!')

if __name__ == '__main__':

    d = Dog()
    print(d.run())
