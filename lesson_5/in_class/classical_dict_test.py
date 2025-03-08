import random
from collections import defaultdict

# lst = []
# for num in range(20):
#     result = random.randint(1, 20)
#     lst.append(result)
#
# dict_list = defaultdict(list)
#
# for k in lst:
#     if k >= 10:
#         dict_list['bigger than 10'].append(k)
#     else:
#         dict_list['smaller than 10'].append(k)
#
# print(dict_list)

# lst = []
# for num in range(20):
#     result = random.randint(1, 20)
#     lst.append(result)
# db_dict={'bigger than 10':[],'smaller than 10':[]}
# for num in lst:
#     if num >= 10:
#         db_dict['bigger than 10'].append(num)
#     else:
#         db_dict['smaller than 10'].append(num)
# print(db_dict)
'''RanDom Car Plate No'''
lst = []
for i in range(1, 101):
    province = random.sample('甘湘京沪港青鄂苏滇浙粤', 1)[0]
    types = random.sample('ABCDEFG', 1)[0]
    dot = '.'
    car_No = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 5)
    new_No = ''.join(car_No)
    plate_No = province + types + dot + new_No
    lst.append(plate_No)

'''统计车牌'''
dc = {}
for car in lst:
    if dc.get(car[0]):
        dc[car[0]] += 1
    else:
        dc[car[0]] = 1
print(dc)
