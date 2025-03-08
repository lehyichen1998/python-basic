'''

python的 常用框架:
    小全栈:
    web: django  --> 精装修 --> 集成了很多功能 (重量级框架framework)
         flask --> 简单 --> 手动去配置，添加对应的代码(轻量级框架framework)
    前端：
        bootstap ; vue.js ; layui(模板)
    服务器；
        部署; sql 语句；

    爬虫:
        scrapy: (重量级的爬虫框架)
        requests :  模块;


    1:pip install flask

'''
# 创建一个flask的app  -->web application

from flask import Flask

appsss = Flask(__name__)

# 配置路由 -- >什么是路由？  概念: 通过路径的形式访问某一个服务下面的 文件
@appsss.route('/eat')
def eat():
    return '我正在吃饭~'

@appsss.route("/")
def first():
    return 'hello world'
@appsss.route('/sleep')
def sleep():
    return '我想睡觉~'


# 开启flask服务
'''
url: http://localhost:5000/
http:   是一种网络协议; https
127.0.0.1 : 本机
:5000 表示是端口;
'''
appsss.run()





