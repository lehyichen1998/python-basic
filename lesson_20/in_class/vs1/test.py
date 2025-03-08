'''

'''

from pyecharts.charts import Bar
from random import randrange

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

bar.render('商家的销售数据.html')
