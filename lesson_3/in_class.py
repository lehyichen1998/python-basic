# lst = ['小红', ('小绿'), [7, 8, 9], {"name": '大熊', "age": 60, "score": 0}]
# print(lst[3]["name"])
# print(lst[2][1])

drink_100plus = ['100plus', 5, '123456', '2020']
drink_cola = ['cola', 3, '654321', '2021']

# drink_100plus.append('已购买') # ['100plus', 5, '123456', '2020', '已购买']
# drink_100plus.insert(1,'asddd') # ['100plus', 'asddd', 5, '123456', '2020']
# drink_100plus.append(drink_cola) # ['100plus', 5, '123456', '2020', ['cola', 3, '654321', '2021']]
# drink_100plus.extend(drink_cola) # ['100plus', 5, '123456', '2020', 'cola', 3, '654321', '2021']
# drink_100plus.pop() #auto delete last one data(['100plus', 5, '123456'])
# drink_100plus.pop(2) # ['100plus', 5, '2020']
# drink_100plus.remove('123456') # ['100plus', 5, '2020']
# drink_100plus[0] = '100plas++++' # ['100plas++++', 5, '123456', '2020']
# drinks_name = drink_100plus[0] # 100plus
# print(drink_100plus[:-2]) #['100plus', 5]
# print(drink_100plus[2:]) # ['123456', '2020']
# print(drink_100plus[::-1]) # ['2020', '123456', 5, '100plus']

# lst = ['小红', ('小绿'), [7, 8, 9], {"name": '大熊', "age": 60, "score": 0}]
# print(lst[2][0]) # 7
# print(lst[3]["name"]) # 大熊

# for_lst = [num for num in range(1,11)]
# print(for_lst)

# result_lst = [num**2 for num in range(1,101)]
# print(result_lst)

from pyecharts.charts import Pie

goods = ['保温杯', '枸杞', '洗发水', '格子衬衫']
sale_count = [50, 60, 40, 200]

# zip() combine goods and sale_count
show_data = list(zip(goods, sale_count))

Pie().add(series_name='程序员套装销量排行',data_pair=[data for data in show_data]).render('lesson3_assignment.html')

