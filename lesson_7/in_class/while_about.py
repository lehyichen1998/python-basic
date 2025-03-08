'''    while      '''
# num =1
# while num < 3:
#     print('今天好想你!!!!!!!!!!!!!!!!!!!!!!!')
#     num += 1

'''           '''
# num = 1
# sums = 0
#
# while num <= 10:
#     sums = sums+num
#     print(sums)
#     num +=1
#
# print('Total: ',sums)
#
# count = 0
# sums = 0
#
# while count < 100:
#     if count % 2 == 0:
#         sums = sums + count
#     count += 1
# print(sums)
'''             '''
# count = 0
# print('---请进行登录---')
# while count < 3:
#     password = input('请输入您的密码》》》》》》》》》》》')
#     if password == '123':
#         print('密码正确~~~~~~~~欢迎登录！！！！！！！')
#         break
#     else:
#         print('密码错误~~~~~~~~请重新输入！！！！！！')
#     count+= 1
#
# count = 0
# while count < 5:
#     if count == 3:
#         print('今天太快了吧!!!!!!!!!!!!!!!!!!!!!')
#         continue
#     count +=1
#

# for i in range(5):
#     print('外外外外外外层循环 %d' % i)
#     for j in range(5):
#         print('内内内内内层循环 %d' % j)

# i = 0
# while i <3:
#     print('外外外层循环~',i)
#     for j in range(3):
#         print('内内内层循环~',j)
#     i+=1
#
# i = 0
# while i < 3:
#     print('外外外层循环~', i)
#     j = 0
#     while j < 3:
#         print('内内内层循环~', j)
#     j += 1
#     i += 1

dc = {'name': '大熊', 'age': 160, 'hobby': 'sleep'}
# for i in dc:
#     print(dc[i])
count = 0
# while count < len(list(dc.keys())):
#     key = list(dc.keys())[count]
#     value = dc[key]
#     print(key ,':',value,end=' ')
#     count +=1

language = ['java','python','c','html','sql',]
counts = 0
while counts< len(language):
    value = language[counts]
    print(value,end=' : ')
    counts+= 1

