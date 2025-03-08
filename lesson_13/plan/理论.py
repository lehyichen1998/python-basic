
'''
一 ：文件(file)I/O
    -就是python对计算机中的文件，写入，写出
        -I/0(input/output)
    import os
    os.mkdir('代码创建文件夹')
    import os
    os.rmdir('代码创建文件夹')  # 删除刚才的文件夹
二 ：文件操作：
    (txt，execl，world，ppt；
    字符流，   二进制：mp3，.jpg .mp4)
        第一：认识 open
        第二：认识路径
        第三：读和写
        第四：练习
            -操作文件的步骤
                -先找到，并打开文件
                -打开文件进行读写操作
                -关闭文件
            -异常处理
'''

'''
文件方面的单词词汇：
open  close  write  read  等等
例如打开一个文件的语法  open('文件名',mode='r(默认为read)'encoding='编码形式')
mode的格式和他们的作用：
    ’r‘:  读取一个文件
        文件阅读：
        a=open('安徽省.csv',mode='r',encoding='utf-8')
        print(a.read())
        a.close()
    'w':  文件写入，它会自动判断是否存在该文件，如果存在就消除里面的文字重新
           写入现在的文字，如果不存在就新建以这个文件名的文件，并且写入现在
           的文字
        文件写入：
        b=open('x.txt',mode='w',encoding='utf-8')
        b.write('aaaaaaa')
        b.close()
        重写一遍就会发现它更换了
        b=open('x.txt',mode='w',encoding='utf-8')
        b.write('bbbbbbb')
        b.close()
        缺点：只能一次性添加，不然在文件后面进行添加
        问题：
        b=open('x.txt',mode='w',encoding='utf-8')
        b.write('bbbbbbb')
        b.write('aaaaaaa')
        b.close()
        最后显示是什么？
        觉得是7个b 的扣  1   觉得是  7个a的扣  2  觉得都有的扣 3
    'b':  二进制类型的   例如：图片,视频,音乐等等下载会需要以二进制下载
         具体会在爬虫中会使用，其他地方用的少
    'a'  文件信息加入：
         同样会判断是否存在该文件，如果不存在就新建，如果存在就会在信息的后面
         进行添加信息
         b = open('m.txt', mode='a', encoding='utf-8')
         b.write('bbbbbbb')
         b.write('aaaa')
         b.close()
由于每次打开文件都会需要用close关闭，然后如果没有关闭的话就会出现文件损失等状况
所有针对这个问题可以用下面这个方式
with open():
with open()就会自动关闭打开的这些文件
'''
