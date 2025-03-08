from pyecharts.charts import Bar
from random import randrange
from flask import Flask, render_template

data_app = Flask(__name__, static_folder="../templates")

bar = (
    Bar()
        .add_xaxis(['衬衫', '卫衣', '裤子', '鞋子', '帽子'])
        .add_yaxis('商家A', [randrange(10, 80) for i in range(5)])
        .add_yaxis('商家B', [randrange(10, 80) for j in range(5)])
        .add_yaxis('商家C', [randrange(10, 80) for k in range(5)])
        .add_yaxis('商家D', [randrange(10, 80) for v in range(5)])
        .add_yaxis('商家E', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('商家F', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('商家G', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('商家H', [randrange(10, 80) for _ in range(5)])
)


@data_app.route('/')
def index():
    return render_template('data_vasul.html')


@data_app.route('/data')
def return_data():
    print('响应了数据到页面上去!!!')
    b = bar
    print(b.dump_options_with_quotes())
    return b.dump_options_with_quotes()


data_app.run()
