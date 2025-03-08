# navicat 下载; https://www.navicat.com.cn/download/navicat-for-mysql

# navicat 破解: https://my.oschina.net/u/4275654/blog/4316363

# 建立一个连接，连接到我们安装的mysql服务;

# navicat:是 sql：ide ，不仅可以链接 mysql，Oracle，sqlite，

#  ;   :

'''# python 链接 mysql'''

# pip install pymysql；

# 创建链接

import pymysql as mysql

conn = mysql.connect(
    host='127.0.0.1', # localhost 表示链接的主机地址;
    user='root',
    password='admin',
    charset='utf8mb4'
)
# 创建游标对象
coursor = conn.cursor()


# 创建一个数据库;
sql = 'create database if not exists db_7;'   # 默认创建

# 删除数据库

drop_database = 'drop database db_9;'  #

# 通过游标对象获取链接对象

coursor.execute(drop_database)
print('创建成功~')
# 关闭与数据库之间的链接
coursor.close()



