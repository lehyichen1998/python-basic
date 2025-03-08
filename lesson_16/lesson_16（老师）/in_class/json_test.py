'''

json格式：
        json_str = {"name":"小白","age":20,"like_learning":true,"massage":null}
        python字典格式：
        dict_str = {'name':'小白','age':20,'like_learning':True,'massage':none}

        json_str = {"name":"小白","age":20,"favorit":["python","basketball","run"]}

'''
'''
boolean：
    在json中 ：
        true: 小写，false 
    在python：
        True: 大写 ，False

json 全称 叫做 (JavaScript object Notation)：
独立的数据类型：java ，JavaScript
'''
import json
json_str = '{"name":"小白","age":20,"like_learning":true,"massage":null}'


# print(json_str)
# print(type(json_str))

dc_str = json.loads(json_str)       # 1  # 2
dc_test = {'name': '小白', 'age': 20, 'like_learning': True, 'massage': None}
# print(dc_str)
# print(type(dc_str))

# 将dict数据转换成 json数据；
json_s = json.dumps(dc_test)
print(type(json_s))
print(json_s)

