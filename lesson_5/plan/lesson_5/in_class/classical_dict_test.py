'''
    字典的案例：
'''
# 利用字典来实现数字大小的区分，并保存 {'大于10数据':[0,1,2,3,4,5,6,7,8,9],'小于10的数据':[11,12,12.1,13]}

# 创建随机数据
# import random
# from collections import defaultdict
#
# # 创建10个1-20的随机数
# lst = []
# for i in range(20):
#     result = random.randint(1, 20)
#     lst.append(result)
# # 把大于10的数据放在一边 小于10的数据又放在另外一边
# dict_list = defaultdict(list)
# # print(dict_list)
# for k in lst:
#     if k >= 10:
#         dict_list['大于10的数据'].append(k)
#     else:
#         dict_list['小于10的数据'].append(k)
# print(dict_list)

# 利用字典来实现数字大小的区分 ；第二种实现方式、
# import random
# lst = []
# for i in range(20):
#     result = random.randint(1, 20)
#     lst.append(result)
# # 创建一个字典接接收数据；
# db_dict = {'大于10': [], '小于10的数据': []}
# for num in lst:
#     if num >= 10:
#         db_dict['大于10'].append(num)
#     else:
#         db_dict['小于10的数据'].append(num)
# print(db_dict)



'''     随机车牌        '''
# 生成 随机的省份
import random
# sample .随机任何一个值 ，以列表的形式进行返回；
lst = []
for i in range(100):
    province = random.sample('甘湘京沪港青鄂苏滇浙粤',1)[0]
    types = random.sample('ABCDEFG',1)[0]
    dot = '.'
    car_numbers = random.sample('ABCDEFGOPQRSTYVWXYZ0123456789',5)
    # print(car_numbers)
    new_number = ''.join(car_numbers)
    # print(new_number)
    plate_number = province+types+dot+new_number
    lst.append(plate_number)

'''    统计车牌来自的地区的案例     '''
# 创建dc字典保存统计数据；
dc = {}
for car in lst:
    # print(car[0])
    if dc.get(car[0]): # 如果当前 地区存在 次数＋1
        dc[car[0]] = dc[car[0]] + 1
    else:
        # dc[car[0]] 相当于字典的key值；1 相当于value；
        dc[car[0]] = 1
