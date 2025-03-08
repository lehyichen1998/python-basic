import os

# db_file = 'stu_database.txt'
# print(os.path.exists(db_file))


# with open(db_file, 'r', encoding='utf-8') as r_file:
#     stu_lst = r_file.readlines()
#
# print(stu_lst)


# format_title = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
#     print(format_title.format('id', '姓名', 'c成绩', 'python', 'html', '总成绩'))


# lst = [{1, 3, 5}, {2, 4, 6}, {10, 20, 30}]
# lst.sort(reverse=False)
# print(lst)

# lst = ['aaa', 'aaaa', 'aaaaa']
# lst.sort(key=len, reverse=True)
# print(lst)

lst = ["{'id': '1', 'name': '1\t', 'c': 1, 'python': 2, 'html': 3}\n",
       "{'id': '2', 'name': '2', 'c': 1, 'python': 2, 'html': 4}\n"]
new_lst = []
for dc in lst:
    item = dict(eval(dc))
    new_lst.append(item)


def max_and_small(dc_obj):
    return dc_obj['html']


new_lst.sort(key=max_and_small, reverse=True)
# new_lst.sort(key=lambda x: int(x['html']), reverse=True)
print(new_lst)
