# https://kkdaj.lanzous.com/ic03rbi cracker navicat version
# pip install pymysql
import pymysql as mysql

conn = mysql.connect(
    host='127.0.0.1',
    user='root',
    password='106055lyc',
    charset='utf8mb4'
)

coursor = conn.cursor()

create_sql = 'create database if not exists db_7;'
delete_sql='drop database db_7'
coursor.execute(create_sql)
print('创建成功~')
coursor.close()
