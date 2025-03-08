# 导入狗狗的模块
from 基础课程.lesson_15.in_class_15.类的继承.B import Dog
# 创建一个哈士奇类

class hashiqi(Dog):
    ''' 说明哈士奇的类 fansha的这个方法重写 dog类中的犯傻方法
        优从当前文档中索取方法
    '''
    def fansha(self):
        print('哈士奇犯傻')
    def chaijia(self):
        print('哈士奇正在拆家')


h = hashiqi()
h.fansha()
