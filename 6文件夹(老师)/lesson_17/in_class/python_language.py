# 判断文档是否存在
import os

db_file = 'stu_database.txt'
# print(os.path.exists(db_file))


# with open(db_file, 'r', encoding='utf-8') as r_file:
#     stu_lst = r_file.readlines()  # 一行[{},{},{}]
#     for i in stu_lst:
#         print(type(dict(eval(i))))
# print(stu_lst)

# d ={'ids': '3', 'name': '3', 'c': 3, 'python': 3, 'html': 3}
# print(d.get('ids'))

# d2 = {'id': '2', 'name': '2', 'c': 2, 'python': 2, 'html': 2}
#
# print(d['id'] =='4')


# 定义的标题输出格式

# format_title = '{:^10}\t{:^20}\t{:^30}\t{:^6}\t{:^6}\t{:^6}\t'
#
# print(format_title.format('id', '姓名', 'c成绩', 'python', 'static', '总成绩'))
#

# 关于排序

# 1认识排序
# lst = [1, 3, 5, 7, 9]
# lst.sort(reverse=False)
# print(lst)

# 2特殊元素排序
# lst = [{1,3,5},{2,4,6},{10,20,30}]
# lst.sort(key=len,reverse=True)
# print(lst)

# 3认识key参数
# lst = ['aaa','aaaaa','aaaaaa']

# lst.sort(key=len,reverse=False)
# print(lst)

# str 1  ,dc  2
lst = ["{'id': '3', 'name': '胖虎\t', 'c': 0, 'python': 1, 'html': 2}\n","{'id': '4', 'name': '4', 'c': 4, 'python': 4, 'html': 4}\n"]
new_lst = []
for dc in lst:
    item = dict(eval(dc))
    new_lst.append(item)


def max_and_min(x):
    return x['html']

new_lst.sort(key=max_and_min,reverse=True)




print(new_lst)
