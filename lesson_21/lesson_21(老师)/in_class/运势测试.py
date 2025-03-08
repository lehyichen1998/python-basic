# coding=utf-8
# flask后端框架实现; request 请求模块,render_template 返回页面的模块;
from flask import Flask, request, render_template
# requests是爬虫的抓包模块;
import requests

luck_app = Flask(__name__)


@luck_app.route('/')
def data():
    # 接受前端传递的数据;
    consname = request.args.get('consName')
    types = request.args.get('types')
    # 创建页面;
    print(consname, types)
    # 第一种可能表示没有参数输入,显示默认查询数据;
    if consname is None and types is None:  # 表示没有参数输入,显示默认查询数据
        result = requests.get(
            'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=天秤座&type=today')
        # 将json数据转换成 dict;
        name = result.json()['name']
        color = result.json()['color']
        datetime = result.json()['datetime']
        summary = result.json()['summary']
        print('请求的星座名称:%s,color%s,datatime%s,summary%s :' % (name, color, datetime, summary))
        #                                  name 传递到页面name
        return render_template('today.html', name=name, color=color, datetime=datetime, summary=summary)
    # 第二种;
    elif consname != '' and types == 'today':
        result = requests.get(
            'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=%s&type=%s'
            % (consname,types) )
        name = result.json()['name']
        color = result.json()['color']
        datetime = result.json()['datetime']
        summary = result.json()['summary']
        print(name)
        print(color)
        print(datetime)
        print(summary)
        return render_template('today.html', name=name, color=color, datetime=datetime, summary=summary)
    # 第三种
    elif consname != '' and types == 'tomorrow':
        result = requests.get(
            'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=%s&type=%s'
            % (consname, types))
        name = result.json()['name']
        color = result.json()['color']
        datetime = result.json()['datetime']
        summary = result.json()['summary']
        return render_template('today.html', name=name, color=color, datetime=datetime, summary=summary)
    # 本周运势
    # 本月运势
if __name__ == '__main__':
    luck_app.run()
