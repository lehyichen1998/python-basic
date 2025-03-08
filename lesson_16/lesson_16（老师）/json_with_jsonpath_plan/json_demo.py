'''

什么是json？
    json的类型跟python中的字典长得非常的像但是又不是字典
    例“
        json格式：
        json_str = {"name":"小白","age":20,"like_learning":true,"massage":null}
        python字典格式：
        dict_str = {'name':'小白','age':20,'like_learning':True,'massage':none}

        json_str = {"name":"小白","age":20,"favorit":["python","basketball","run"]}

json在python中的常用方式：
    1.编码(encode)：把一个python对象编码转换成json字符串 json.dumps()
    2.解码(decode)：把json格式字符串解码转换成python对象 json.loadS()
    dumps()  domp是将 Python的数据类型转换为 json
    loads()  load是将 json数据转化为 json
'''
import json
#json实例
# 字典格式：
dict_str = {'name':'小白','age':20,'like_learling':True,
            'massage':None,"账号":123456,"密码":654321,
            'txt':'dasdasdasdsadadasdasdasdasdasdasdas'
                  'asdasdasdsadasdasdasdasdasdasdasd'
                  'asdsadasdasdasdasdsadasdasdasdsad'}
# print(type(dict_str))
#json格式：
json_str = json.dumps(dict_str)
# print(json_str)
#将json转换为 dict
dc = json.loads(json_str)
print(dc)