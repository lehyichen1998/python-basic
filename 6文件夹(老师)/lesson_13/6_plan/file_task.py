
'''
文件夹的创建和删除
    import os
    # os.mkdir('我的新文件夹')

    # os.rmdir('我的新文件夹')
认识 open

'''
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 文件名称，
# mode 模式'r','w','a'
# buffering   流： 字（byte）节流 input、output
# encoding = 字符编码？ ’utf-8‘,'gbk'
# newline = #另起新的一行 ''


# 认识路径 ： 绝对路径   和  相对路径；
# location = 'D:\基础课程\第12文件和异常\三期\我的文档' #绝对路径
# loc = '我的文档' # 相对路径
# loca = r'D:\基础课程\第12文件和异常\file3\test.txt'  #转义符 出错
# lo = '../file3/test.txt' #相对路径
# 拿c盘中的文件
# lc = r'C:\test1.txt'
#
# file = open(lc,mode='r',encoding='utf-8')
# print(file.read())

# 写入文件
# b = open('x.txt', mode='w', encoding='utf-8')
# b.write('888888')
# b.write('5555555')
# b.close()  #关闭文档

'''
由于每次打开文件都会需要用close关闭，然后如果没有关闭的话就会出现文件损失等状况
所有针对这个问题可以用下面这个方式
with open():
with open()就会自动关闭打开的这些文件
'''

# 利用 with open()来实现对文档的读和写
# loca = r'D:\基础课程\第12文件和异常\file3\test.txt'
# with open(loca,'r',encoding='utf-8') as r_file:
#     r = r_file.read()
#     print(r)
#     with open('我的文档','w',encoding='utf-8') as w_file:
#         w_file.write(r)

'''
read()一口气读完文档里所有的内容
read() 只读文档的第一行 内容，并以列表的形式返回；
readlines()读完数据是以列表的形式进行返回
'''
# loca = r'D:\基础课程\第12文件和异常\file3\test.txt'
# with open(loca,'r',encoding='utf-8') as r_file:
#     r = r_file.readlines()
#     with open('我的文档','w',encoding='utf-8') as w_file:
#         for i in r:
#             w_file.write(i)

#对音乐文件进行处理；
'''
那么之前我们open默认方式主要还是针对的文本进行处理
那么我需要处理视频，音乐，图片这种文件怎们办？
在处理这些文件之前我们要知道他们是以什么形式来的
1看到我们的音乐文件；
注意：
    任何视频，音乐，图片都是以二进制的文件进行读写：
    包括我们的文本以及任何数据；
那么我们如何读取二进制的这些文件呢？
其实只要在mode上加上 ’b‘就好了，这样就可以读取大型的文件
'''
#读写二进制的音乐文件  实现复制粘贴过程；
with open('../in_class/Ferrari.mp3', mode='rb') as m_mp3:
    r = m_mp3.readlines()
    with open('法拉利.json',mode='wb') as f:
        for i in r:
            f.write(i)
#读写二进制视频文件
with open('test_vedio.mp4',mode='rb')as v:
    r_v = v.readlines()
with open('vedio.txt',mode='wb') as vs:
    for i in r_v:
        vs.write(i)
    print('文件写入成功')


# 文件与异常；
# lc = r'D:\新基础课程\lesson_12file_except\三期\x.txt'
# try:
#     # 截取异常
#     with open(lc, 'r', encoding='utf-8') as r_file:
#         print(r_file.read())
# except Exception as e :
#     print('没有找到该文件~' ,e)



# 拓展部分；
# 从网页上下载一张图片
# 读二进制数据；
# import os
# import requests
# cg_dir = os.mkdir('曹格图片')
# url = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2920806161,3573117881&fm=26&gp=0.jpg'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
# }
# respone = requests.get(url,headers = header)
# jpg_name = '曹格1'
# with open('曹格图片'+'./'+jpg_name+'.jpg','wb') as w_f:
#     w_f.write(respone.content)
# print(respone.content)
# with open(cg_dir + './'+respone.,'wb')



# 异常处理
# 制造一个 异常 让控台产生报错，这个时候 载使用 try  except 对 异常进行捕获；
# try:
# <语句>        #运行别的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生


# 实现不断的向一个文本中添加数据；
def user_input():
    while True:
        a = input('请输入一段诗歌：')
        if a != '':
            w_f = open('2.txt',mode='a',encoding='utf-8')
            w_f.write(a+'\n')
            w_f.close()
        else:
            break

if __name__ == '__main__':
    user_input()














