'''
tuple:
    list 和 tuple非常的相似；
    list = []
    tuple = ()
    lst 支持 真删改查；tuple 不支持 增删改；
    tp = ('sads',12312,[],(),{},float,bool,)
    总结：
        tuple 它的数据类型更加安全；

dict:(dictionary)
    key ： value
    dict的声明方式：
        # 以逗号进行隔开，每隔一个逗号代表为一个元素；
    dc = {'key':'vlaue','name':'大雄',}



'''

'''元组类型：'''

# tp = ('sads', 12312, [1, 2, 3], (), {}, float, bool,)
# # 元组 （tuple）多维查询；
# # print(tp[2][1])
# num1 = ('1',)
# print(type(num1))


'''dict：
    关于字典的增删改查；
'''
# 字典的查询；
dc = {'name': '哆啦A梦', 'age': 60, 'hobby': ['help_大雄', 'coding', '铜锣烧'], 'mark': {'python': 99, 'html': 100}}
# for item in dc:
#     print(dc[item])

# 拿python成绩；
# print(dc['mark']['python'])

# 字典对象的增加；

# dc.setdefault('smart')  # 增加key
# dc['smart'] = True
# print(dc)

# 字典删除元素
# dc.pop('age')
# print(dc)

# dc.popitem()
# print(dc)

# del dc['hobby']
# print(dc)

# 字典中的修改
# dc['age'] = 200
# print(dc)

# dc.update({'name': '机器猫'})
# print(dc)

# tuple;list;dict; 转换关系；
tup = (['one', 10], ['tow', 20], ['three', 30])
lst = [['one', 10], ['tow', 20], ['three', 30]]
# print(type(tup))

# 将当前tuple 转换成 字典类型 {'one':10,'tow':20}

# s = '1'
# print(type(int(s)))

# print(dict(tup)) # tuple转字典格式；
# print(dict(lst))  # lst类型转换；


