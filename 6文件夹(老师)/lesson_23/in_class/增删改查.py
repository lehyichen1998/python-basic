''' 进行增删改查的操作   '''


# 定义链接MySQL的函数
def my_connect():
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='admin',  # 密码是自己在安装的时候的密码
        port=3306,
        database='db_7',  # 指定链接的数据库名
    )
    return conn


c = my_connect()


# c.close()  # 关闭数据库的链接对象;
# print(c)

# 增加的操作
def add():
    # 获取链接对象
    conn = my_connect()
    cur = conn.cursor()  # 生成游标对象
    # 增加的操作，向数据库中增加哆啦A梦的数据
    sql = "insert into tb_stu values(6,'T仔',20,20)"
    try:
        # 执行sql语句
        cur.execute(sql)
        conn.commit()
        print('成功插入数据')
    except Exception as err:
        print('添加数据失败', err)
        # 如果发生错误，将事务进行回滚(取消提交)
        conn.rollback()
    conn.close()


# 删除的操作
def delete():
    # 获取数据库的连接
    conn = my_connect()
    # 创建游标
    cur = conn.cursor()
    # 删除 T仔
    ids = 9
    sql = "DELETE FROM tb_stu where stu_id = %d" % ids
    try:
        # 执行sql语句
        cur.execute(sql)
        # 执行好的sql语句提交到数据库中
        conn.commit()
        print('id 为 %d 删除成功' % ids)
    except Exception as err:
        print('删除发生了错误',err)
    conn.close()

# 修改的操作
def update():
    conn = my_connect()
    cur = conn.cursor()
    # sql
    sql = "update tb_stu set stu_name = '大雄' where stu_id = 1"
    try:
        cur.execute(sql)
        conn.commit()
        print('修改成功')
    except Exception as err :
        print('修改失败',err)
    conn.close()
# 查询的操作
def select():
    conn =  my_connect()
    cur = conn.cursor()
    # 查询语句
    sql = 'select * from tb_stu;'
    try:
        cur.execute(sql)
        data = cur.fetchall()
        print(type(data))
        for i in data:
            print(i)
    except Exception as err:
        print('查询错误',err)
if __name__ == '__main__':
    # add()
    # delete() #
    # update()
    select()