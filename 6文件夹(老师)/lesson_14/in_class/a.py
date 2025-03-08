# 我们也可以自己去制作一些模块
from oop_test import Person

# 1 ，2 ，3

# 自己编写模块
'''
 1 : 当前的pycahrm 配置的python解释器 是哪一个 例如我的是 3.6 
 2 : 打开 cmd where python ： 找到路径
 3 : 打开 此电脑的python文件位置 
        C:\Users\Administrator\AppData\Local\Programs\Python\Python36\python.exe
        C:\Users\Administrator\AppData\Local\Programs\Python\Python36
        去配置 lib 文件夹中的模块 ：
        将 oop.py的这个文件 复制进去；
'''

p = Person()
print(p.say_hello())

