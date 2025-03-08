# os 模块操作文件夹
# import os
# for i in range(5):
#     os.rmdir('lesson_%s_test' % (int(i) + 13))

'''
认识open
    open()：  函数;
    . open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
    函数的= 表示 参数默认的值；
    file : 表示文件路径；
    mode : 表示模式 ，Additional  write  read  binary 等等
    ， w  = write ： 写
    ， r  = read 读
    ， a  = Additional 追加
    ， b  = binary  二进制的格式；
    buffering : 表示 流 ： 字符流 ： byte ；
    encoding :编码格式； utf-8 ,gbk ,GBK,

认识路径：
    # 相对路径；
        定义：
            在和 本文件 同一目录下 创建文件夹
            import os
            os.mkdir('6_test')
            在非同一目录下 创建文件夹；
            import os
            os.mkdir('../../lesson_14/6test')
    # 绝对路径；
        定义：
            在计算中 文件盘符中绝对指定一个地方 ;
            import os
            os.mkdir(r'E:\6test')   # 反斜杠是python中的转译符号
open中的读和 写；

'''

''' 
    ， w  = write ： 写 
        属性：
            没有文档的情况下 ，默认创建一个文档；
            有文档的情况下，默认覆盖之前的文件数据；
            file = '上课的测试文件.txt'
            w_file = open(file,mode='w',encoding='utf-8')
            w_file.write('感谢同学们送的花花')
            w_file.close()
    ， r  = read 读
        属性:
            read()
            readline()
            readlines()
    ， a  = Additional 追加
        a_file = open('test.txt','a+',encoding='utf-8')
        for i in range(5):
            a_file.write(str(i)+'\n')
    ， b  = binary  二进制的格式；
        
'''
# # 追加
# a_file = open('test.txt','a+',encoding='utf-8')
# for i in range(5):
#     a_file.write(str(i)+'\n')

# 爬虫 -- >模拟浏览器 --->访问服务器  pip install requests
# 反爬虫 机制  破解办法 -- 为代码来个 伪装头部；
import requests  # 抓包该工具
# url 表示连接地址
url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2198214324,155280513&fm=26&gp=0.jpg'
# 请求头
header = {
    # 请求头封装的是 当前的计算机信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
respones = requests.get(url,headers=header)
print(respones)

# 创建文件夹 保存二进制文件数据

import os
os.mkdir('zxc图片')
photo_local = 'zxc图片'
zxc = 'zxc_ph'
w_p = open(file=photo_local+'/'+zxc+'.jpg',mode='wb')
w_p.write(respones.content)
w_p.close()

# 异常处理；
'''  是对一个 可能会存在报错的 地方代码的预处理  
try:
    可能会报错的代码
excpet: 
    报错后执行的代码
 
'''

try:
    r_file = open('上课的测试文件.tx','r',encoding='utf-8')
    print(r_file.read())
except FileNotFoundError:
    # 当 FileNotFoundError 错误出现了的时候 执行 except 里面的代码模块
    print('文件出现了路径问题')
except FutureWarning:
    print('文件出现了警告')
else:
    print('可能出现了其他的文件错误')



