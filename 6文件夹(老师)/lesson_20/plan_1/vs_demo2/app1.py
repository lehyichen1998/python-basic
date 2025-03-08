from random import randrange

#导入flask库
from flask import Flask, render_template
#导入可视化模块库
from pyecharts.charts import Bar
import random
# html静态页面地址
html_location = 'vasul_data.html'
#配置flask地址
app = Flask(__name__, static_folder="../templates")
# li = ['羊毛衫','羽绒服','格子称衫','雪地靴','帽子','围巾']
#定义柱状图函数
def bar_base():
    c = (
        Bar()
        #先定义一些随机数组，用于产生数据方便等下进行查看
        .add_xaxis(["衬衫", "羽绒服", "卫衣", "裤子", "牛仔裤", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .add_yaxis('商家C', [randrange(0, 100) for _ in range(6)])
        .add_yaxis('商家d', [randrange(0, 100) for _ in range(6)])
        .add_yaxis('商家e', [random.randint(50,100) for _ in range(6)])
    )
    return c

#配置路由
@app.route("/")
def index():
    return render_template(html_location)

#接收来自页面的数据（barChart）
@app.route("/barChart")
def get_bar_base():
    c = bar_base()
    return c.dump_options_with_quotes()  #将数据返回

if __name__ == "__main__":
    app.run()