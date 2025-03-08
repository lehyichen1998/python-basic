# 解除注释：ctrl+/
'''
list:
    认识list：将list看成一个锅；
                锅中的食物，我们看成 元素；
    lst = []
    在list中插入数据;
认识索引；
    index；
    lst = ['小红',('小绿'),[7,8,9],{"name":'大雄','age':60,'score':0}]
    index :   0   ,   1  ,    2   ,          3
'''
# 在list中插入数据;
# lst = ['小红', ('小绿'), [7, 8, 9], {"name": '大雄', 'age': 60, 'score': 0}]
# print(lst)

# 索引：
# lst_first = lst[0]
# print(lst_first)

'''
列表的增删改查：
'''
# drink_mai = ['脉动', 5, '123456', '2020']
# drink_cola = ['cola', 3, '654321', '2021']

'''         列表增加的操作         '''
# 自然顺序增加；
# drink_mai.append('md123')
# print(drink_mai)

# 指定索引增加方式；
# drink_mai.insert(2,'水蜜桃风味')
# print(drink_mai)

# 列表增加列表数据；
# drink_mai.extend(drink_cola)
# print(drink_mai)

'''         列表的删除       '''
# drink_mai.pop(2)  # 默认删除最后一条信息；
# print(drink_mai)
# drink_mai.remove('123456')  # 根据元素进行删除
# print(drink_mai)
# drink_mai.clear()   # 将整个列表清空；
# print(drink_mai)

'''            列表的修改操作         '''
# 在列表中只能够根据 索引进行修改；
# drink_mai[0] = '脉动-水蜜桃味'
# print(drink_mai)

'''            列表的查找操作           '''
drink_mai = ['脉动', 5, '123456', '2020']
drink_cola = ['cola', 3, '654321', '2021']

# drinks_name = drink_mai[0]
# print(drinks_name)
#  这是查找索引的方式；
# print(drink_mai.index('脉动'))   # index是根据 元素，去查找 索引值；
# 列表的区域查找； 也叫做切片操作；
'''切片的索引是以1开始而不是0'''
# 取 这个数据：['脉动', 5]
# print(drink_mai[:-2])
# 取 这个数据 '123456', '2020'
# print(drink_mai[2:])

# 顺序的反响查询；
# print(drink_mai[::-2])   # ['2020', '123456', 5, '脉动']
'''二维查询，三维，四维查询'''
# lst = ['小红', ('小绿',), [7, 8, 9], {"name": '大雄', 'age': 60, 'score': 0}]
#       0         1        2[0]       3['name']
# 如果我想拿到 数字 7 ，
# print(lst[2][0])

# 如果我想拿 大雄；
# print(lst[3]['name'])

'''     列表推导式       '''
# for i in range(10):
#     print(i,end=' ')

# 在一个列表中 实现可迭代数据 储存；
# 列表推导式的写法，
# [变量名  for  变量名  in  range函数数对象(10)]
# lst = []
# for i in range(100):
#     lst.append(i)
# print(lst)

# print([num for num in range(1, 100)])

# 求 1-10000 2次幂
# print(1**2)  # 1的2次方
# print(2**2)  # 2的2次方
# print(3**2)  # 3的2次方
# print(4**2)
#
# result_lst = [num**2 for num in range(1,100)]
# print(result_lst)

'''  
  # 实现商品的 可视化展示；    
  list的可视化用法； 
        1执行命令：pip install pyecharts  
        # pyecharts他是一个可视化模块 库；里面有很多的可视化模块；
        2:需要两组数据
        3:将数据打包
        4:调用Pie()对象；
          
'''
# 导入可视化模块；
from pyecharts.charts import Pie

# 创建两组数据；
goods = ['保温杯', '枸杞', '洗发水', '格子衬衫']
sale_count = [50, 60, 40, 200]
# zip() # 将两组数据打包
show_data = list(zip(goods, sale_count))  # [('保温杯', 50), ('枸杞', 60), ('洗发水', 40), ('格子衬衫', 200)]
                                                # 0                1            2               3
# for i in show_data:
#     print(i)
# 将show_data数据添加到Pie对象中；
# Pie().add(series_name='程序员套装销量排行',data_pair=[data for data in show_data]).render('程序员套装销量排行.html')
Pie().add(series_name='程序员套装销量排行',data_pair=[i for i in zip(goods,sale_count)]).render('程序员套装销量排行.html')

# 用电脑的截图；
