import json

json_str = '{"name":"小白","age":20,"like_learning":true,"message":null}'
print(type(json_str))

dc_str = json.loads(json_str)
print(dc_str)
print(type(dc_str))

dc_test = {'name': '小白', 'age': 20, 'like_learning': True, 'message': None}

json_s = json.dumps(dc_str)
print(json_s)
print(type(json_s))
