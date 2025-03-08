# import os
#
# for i in range(5):
#     os.mkdir('lesson_%s_test' % (int(i) + 13))
# for i in range(5):
#     os.rmdir('lesson_%s_test' % (int(i) + 13))

'''
def add(num1=1, num2=2):
    return num1 + num2
print(add(8, 9))
'''
'''
# import os
# os.mkdir('../plan/6_test')
# os.mkdir('../../lesson_14/6_test')
# os.mkdir(r'D:\6_test')
'''

'''
# file = '上课的测试文件.txt'
# w_file = open(file, mode='w', encoding='utf-8')
# w_file.write('同学们晚上好!!!' + '\n')
# w_file.write('欢迎来到潭州课堂!!!' + '\n')
# w_file.write('老铁双击666!!!' + '\n')
# w_file.close()
'''

'''
file = '上课的测试文件.txt'
r_file = open(file, mode='r', encoding='utf-8')
r = r_file.read()
print(r)
'''

'''
need ask
file = '上课的测试文件.txt'
r_file = open(file, mode='r', encoding='utf-8')
lst_data = r_file.readline()
for i in lst_data:
    print(i,end='')
r_file.close()
'''
'''
a_file = open('上课的测试文件.txt', 'a', encoding='utf-8')
for i in range(5):
    a_file.write(str(i)+'\n')
'''

'''
a_file = open('test.txt', 'a', encoding='utf-8')
for i in range(5):
    a_file.write(str(i) + '\n')
'''

'''
import requests

url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2198214324,155280513&amp;fm=26&amp;gp=0.jpg'
header = {}
response = requests.get(url, header=header)
print(response)

import os

os.mkdir('zxc图片')
photo_local = 'zxc图片'
zxc = 'zxc_ph'
w_p = open(file=photo_local + '/' + zxc + '.jpg', mode='wb')
w_p.write(response.content)
w_p.close()

'''

'''

'''

try:
    r_file = open('上课的测试文件.txt', 'r', encoding='utf-8')
    print(r_file.read())
except FileNotFoundError:
    print('文件出现了路径问题!!!')
except FutureWarning:
    print('文件出现了警告!!!')
else:
    print('可能出现了其他文件错误!!!')
