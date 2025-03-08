'''
python 中的可视化;
    1:就是将大量的数据更直观的展示在我们面前;
    2:传递数据高效，信息更加立体;
    3:python 这门语言：
        matplotlib , matlab , pyecharts--(echarts) ;
    pyecahrts:   https://pyecharts.org/
    echarts: https://echarts.apache.org/examples/zh/index.html


'''
# pip install pyecharts
from pyecharts.charts import Bar
from random import randrange

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

bar.render('商家的销售数据.html')




