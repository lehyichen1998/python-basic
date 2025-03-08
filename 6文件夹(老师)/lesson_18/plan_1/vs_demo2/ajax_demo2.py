from random import randrange
from flask import Flask, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar

# 创建flask项目;
app = Flask(__name__, static_folder="templates")
ajax = "ajax_demo.html"

# 定义数据源
def bar_base():
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(80, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(80, 100) for _ in range(6)])
        .add_yaxis("商家C", [randrange(80, 100) for _ in range(6)])
        .add_yaxis("商家D", [randrange(80, 100) for _ in range(6)])
        # 设置全局 标题；
        .set_global_opts(title_opts=opts.TitleOpts(title="商家销售商品", subtitle="商品销量"))
    )
    return c

# 配置 最基本的路由；
@app.route("/")
def index():
    # 接受到路由/的请求将数据返回到前端页面上
    return render_template(ajax)

# 接收传来的 barChart 参数 ；返回 bar_base数据；
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options()


if __name__ == "__main__":
    app.run()