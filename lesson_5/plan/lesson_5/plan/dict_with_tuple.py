'''
什么是元组？
    元组其实相当于不可变的列表
    元组也是容器类型的数据;
        [],()表示保存很多个数据，中间逗号隔开
    列表：
        增删改查；
    元组：
        查（有序）
        数据会更安全
    字典：
        ditc:全称：dictionary（字典），是一种映射类型的数据
        声明方式：
            变量名 = {'key':'value'}:key,钥匙；vlaue，值

'''
# 元组实例：
import random

'''
tuples = (10,{'name':'小白','age':20,'lst':[1,2,3]},[1,2,3],True,10.1)
print(type(tuples))
#查单个元组里面的数据
print(tuples[1]['lst'][0])
'''
# 字典：
# 字典查询
# a = {'name':'小白','age':20,'faverate':'playing_basketball','mark':{'python':95,'static':80}}
#     # key    vlaue
# print(type(a))
# print(a['mark']['python'])
# #增加：
# a.setdefault('Is_beauty')
# a['Is_buity'] = '漂亮'
# print(a)
# #删除
# a.pop('faverate')
# print(a.popitem())#删除默认最后一个
# print(a)
# del a['faverate']
# print(a)
# a.clear()
# print(a)
# a = {'name':'小白','age':20,'faverate':'playing_basketball','mark':{'python':95,'static':80}}
# #修改：
# a['name'] = '江小白'
# print(a)
# a.update({'mark':{'python':100,'static':100}})
# print(a)

# tuple 转 字典（lst转字典）
tup = (['two', 26], ['one', 88], ['three', 100], ['four', -59])
dic = dict(tup)
# print(dic)
# print(dic['one'])  # 键存在
# print(dic['five'])  # 键不存在

#
# 利用字典来实现数字大小的区分，并保存
from collections import defaultdict  # 自动构建dict函数
import random

li = []
for i in range(20):
    r = random.randint(1, 20)
    li.append(r)
# 把数据中大于10的数字放在一边，小于10的数字又放在另外一边
d_l = defaultdict(list)
# print(d_l)
for i in li:
    if i > 10:
        d_l['大于10的数据'].append(i)
    else:
        d_l['小于10的数据'].append(i)
print(d_l)

'''有序字符生成字典案例'''

# 有字符串"k:1|k1:2|k2:3|k3:4"处理成字典{'k': 1, 'k1': 2....}　
# 转换成字典(面试题) 这里面主要就是一个切割

# str1 = 'k:1|k1:2|k2:3|k3:4'
# dic = {}
# lst = str1.split("|")    #split方法会将切割好的字符串打包成列表
# for i in lst:
#     lst2 = i.split(':')
#     dic[lst2[0]] = lst2[1]
# print(dic)

'''生成随机车牌案例；'''

# 统计每个省的车辆数目
# 随机生成100个车牌，关键部分分为所属地区

# lst = []
# s = ''
# lc = []
# for i in range(100):
#
#     loacl = random.sample('湘沪京黑琼鄂川', 1)[0]  # 随机生成一个地区
#
#     types = random.sample('ABCDEF', 1)[0]  # 随机生成省会城市或者其他城市
#     dian = '.'
#     nums = random.sample('ABCDEFGHIJKLMNOPQRSTYVWXYZ123456789',  5)  # 随机生成车牌号
#     nums = ''.join(nums)
#     # l = [loacl,types,dian,nums]
#     # print(s.join(loacl),s.join(types),s.join(dian),s.join(nums))
#     print(loacl+types+dian+nums)
#     lc.append(loacl+types+dian+nums)
#
#
# print(lc)

'''统计各地区 有多少车牌 '''
cars = ['湘B.1230', '湘B.1230', '湘A.1230', '京A.123', '沪A.784']  # 先手来个列表接收创建各个地区的车牌
# #我们是为了统计每个地区的车牌有多少,来个字典进行统计
# sample :locals1 = {'鲁': '山东', '京': '北京', '黑': '黑龙江'}
dc = {}  # 来个字典接收一下；
for car in cars:
    # 字典对象获取 car列表的第一个元素；如果存在则 为当前的字典key值加1
    # 如果 没有该key 对象 则 创建当前key 对象；
    if dc.get(car[0]):
        dc[car[0]] += 1
    else:
        dc[car[0]] = 1  # 如果下次没有同类车牌，创建当前这类车牌 并附上初始值1
# print(dc)

'''
课后作业案例；
(1)：页面显示 序号 + 商品名称，如：(使用字典或列表)
        1 手机
        2 电脑
(2)： 用户输入选择的商品序号，然后打印商品名称
(3)：用户输入886，退出程序。
'''
# goods = {'1':'格子衬衫','2':'macbook pro','3':'Starbucks coffee'}
# user_want =[]
# while True:
#     for i in goods:
#         print(i,':',goods[i])
#     user = input('请输入你想要的商品>>>')
#     try:
#         print(goods[user])
#         user_want.append(goods[user])
#     except:
#         if user == '886':
#             print('所选商品为%s欢迎下次选购~~'%user_want)
#             break
