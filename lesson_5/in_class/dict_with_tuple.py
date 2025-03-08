# tp = ('sads', 1123123, [1, 2, 3], (), float, bool,)
# print(tp[2][2])

dc = {'name': '哆啦A梦', 'age': 80, 'Hobby': ['Help_大熊', 'coding', '铜锣烧'], 'mark': {'python': 99, 'html': 100}}
# for item in dc:
#     print(dc[item])

# print(dc['mark']['python'])

# dc.setdefault('smart')
# dc['smart'] = True
# print(dc)

# dc.pop('mark')
# print(dc) # {'name': '哆啦A梦', 'age': 80, 'Hobby': ['Help_大熊', 'coding', '铜锣烧']}

# dc.popitem()
# print(dc) # {'name': '哆啦A梦', 'age': 80, 'Hobby': ['Help_大熊', 'coding', '铜锣烧']}

# del dc['Hobby']
# print(dc) # {'name': '哆啦A梦', 'age': 80, 'mark': {'python': 99, 'html': 100}}

# dc['age'] = 100
# print(dc) # {'name': '哆啦A梦', 'age': 100, 'Hobby': ['Help_大熊', 'coding', '铜锣烧'], 'mark': {'python': 99, 'html': 100}}

# dc.update({'mark':{'asd':60,'dsa':80}})
# print(dc) #{'name': '哆啦A梦', 'age': 80, 'Hobby': ['Help_大熊', 'coding', '铜锣烧'], 'mark': {'asd': 60, 'dsa': 80}}

tup = (['one', 10], ['two', 20], ['three', 30])
lst = [['one', 10], ['two', 20], ['three', 30]]
# print(dict(tup)) # tup convert to dict :{'one': 10, 'two': 20, 'three': 30}
# print(dict(lst)) #list convert to dict :{'one': 10, 'two': 20, 'three': 30}
