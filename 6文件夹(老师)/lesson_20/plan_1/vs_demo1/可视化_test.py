'''
python可视化项目

    1什么是数据可视化？、
        将大量的科学数据，商业数据，用图像表示出来，直观展示数据
    2为什么要进行数据可视化
        传递信息高效；信息更加立体；信息更立体
    3python数据可视化的优势
         代码精简：
         众多的第三方库，（例：pyecahrts，matplotlib，都是对整个python实现
         数据展示，提供更加便捷路径）
    整合大量的数据，python之所以简洁是因为整合了大量的第三方库的优势pandas，numpy；

那么可视化类库
      pyecahrts（推荐使用）
          基于百度开源Echarts实现的python版本，支持实现大量的可视化类型
          图表非常丰富，交互效果也非常的棒。

'''
# bar;柱状练习
from random import randrange

from pyecharts.charts import Bar # 导入柱状模块
from pyecharts import options as opts # 导入标题设置

bar = (
    Bar()
    # 所有的数据都是根据x轴来衡量定制的，也就是有多少商品才显示有多少数据
    .add_xaxis(["衬衫", "卫衣", "雪地服", "裤子", "太阳镜", "棉袄"])
    # 那么我们我们定义一些商家他们销售的商品销量数据
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis('商家B',[randrange(10,50) for _ in range(7)])
    .add_yaxis('商家C',[randrange(20,50) for i in range(6)])
    # 设置标题 的名称主标题，副标题；
    .set_global_opts(title_opts=opts.TitleOpts(title="商家名称", subtitle="商家销量信息"))
)
bar.render('商家数据.html')

















