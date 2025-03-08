def my_connect():
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='106055lyc',
        port=3306,
        database='db_7'
    )
    return conn


c = my_connect()


# add
def add():
    conn = my_connect()
    cur = conn.cursor()
    sql = "insert into tb_stu values(5,'humanName',10,20)"
    try:
        cur.execute(sql)
        cur.commit()
    except Exception as err:
        print('添加数据失败', err)
        conn.rollback()
    conn.close()


# delete
def delete():
    conn = my_connect()
    cur = conn.cursor()
    sql = "delete from tb_stu where stu_id =6"
    try:
        cur.execute(sql)
        cur.commit()
    except Exception as err:
        print('删除数据失败', err)
        conn.rollback()
    conn.close()


# update
def update():
    conn = my_connect()
    cur = conn.cursor()
    sql = "update tb_stu set stu_name ='大熊123' where stu_id =1"
    try:
        cur.execute(sql)
        cur.commit()
    except Exception as err:
        print('修改数据失败', err)
        conn.rollback()
    conn.close()


# select
def select():
    conn = my_connect()
    cur = conn.cursor()
    sql = "select * from tb_stu"
    try:
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            print(i)
    except Exception as err:
        print('读取数据失败', err)
        conn.rollback()
    conn.close()


if __name__ == '__main__':
    # add()
    # delete()
    # update
    select()
