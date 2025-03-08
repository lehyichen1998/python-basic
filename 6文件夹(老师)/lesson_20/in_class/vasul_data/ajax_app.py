from pyecharts.charts import Bar
from random import randrange
from flask import Flask,render_template

# 创建flaskapp
data_app = Flask(__name__)  # 如果访问不到你自己定义的html页面加上 static_folder ;自定义的路径;

### wo



bar = (
    Bar()
    # 为x轴添加商品数据
    .add_xaxis(['衬衫','卫衣','裤子','鞋子','帽子'])
    # 添加商家的销售信息
    .add_yaxis('商家A',[randrange(10,80) for i in range(5)])
    .add_yaxis('商家B',[randrange(10,80) for j in range(5)])
    .add_yaxis('商家C',[randrange(10,80) for k in range(5)])
    .add_yaxis('商家D',[randrange(10,80) for v in range(5)])
    .add_yaxis('商家E',[randrange(10,80) for _ in range(5)])
    .add_yaxis('商家f',[randrange(10,80) for _ in range(5)])
    .add_yaxis('商家G',[randrange(10,80) for _ in range(5)])
    .add_yaxis('商家H',[randrange(10,80) for _ in range(5)])
)

# 配置路由
@data_app.route('/')
def index():
    print('刚才页面经过了这个路由')
    # 通过render_template方法将data_vasul.html 响应到页面
    return render_template('ajax_show.html')
# 块标签;
@data_app.route('/data')
def return_data():
    print('响应了数据到页面上去')
    b = bar
    print('执行了bar')
    return b.dump_options()
# bar.render('商家的销售数据.html')
data_app.run()