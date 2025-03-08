# 判断文档是否存在
import os
db_file = 'stu_database.txt'
# print(os.path.exists(db_file))


with open(db_file, 'r', encoding='utf-8') as r_file:
    stu_lst = r_file.readlines()  # 一行[{},{},{}]
    for i in stu_lst:
        print(type(dict(eval(i))))
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






