'''
学生管理系统

'''
import os

file_location = 'student_db.txt'


def menu():
    print('================', '学生管理系统', '===========')
    print('================', '功能菜单', '================')
    print('                 1:录入学生信息              ')  # 增加
    print('                 2:查找学生信息              ')  # 查询
    print('                 3:删除学生信息              ')  #
    print('                 4:修改学生信息              ')
    print('                 5:排序学生信息              ')
    print('                 6:显示所有学生信息           ')
    print('                 0:退出当前系统              ')
    print('===========================================')


def mains():
    while True:
        menu()
        # 当用户进来之后，让其进行选择
        check = int(input('请输入要执行的操作序号:'))
        if check in [0, 1, 2, 3, 4, 5, 6]:
            if check == 0:
                changge = input('你真的要退出当前系统吗？y/n')
                if changge == 'y' or changge == 'Y':
                    print('退出了当前系统，欢迎下次使用')
                    break
                else:
                    mains()
            elif check == 1:

                add()
            elif check == 2:
                select()
            elif check == 3:
                delete()
            elif check == 4:
                update()
            elif check == 5:
                sort()
            elif check == 6:
                alls()
        else:
            print('请输入正确的序号！')


# 对学生信息实现增加操作
def add():
    lst_stu = []
    while True:
        _id = input('请添加学生的id:')
        if not _id:
            break
        _name = input('请添加学生姓名')
        if not _name:
            break
        try:
            c = int(input('请添加学生的c语言成绩'))
            python = int(input('请添加学生的python语言成绩'))
            html = int(input('请添加学生的html语言成绩'))
        except:
            print('您的输入有误，注意不要输入文字')
            continue
        # 将用户输入的信息保存在字典
        stu_dict = {'id': _id, 'name': _name, 'c': c, 'python': python, 'static': html}
        # 列表中储存了很多条字典的数据
        lst_stu.append(stu_dict)
        # 实现多次添加的操作
        # print('当前字典中的数据',stu_dict)
        check = input('还要继续添加学生信息吗？y/n:')
        if check == 'y' or check == 'Y':
            add()
        else:
            print('离开的添加操作！')
            break
        break
    save(lst_stu)


def save(lst):
    # 通过save函数将咱们的数据添加到txt文本当中
    try:
        # 向文件中追加数据
        stu_txt = open(file_location, mode='a+', encoding='utf-8')
        # a+不断的添加
    except:
        stu_txt = open(file_location, mode='w+', encoding='utf-8')
    for i in lst:
        stu_txt.write(str(i) + '\n')
    stu_txt.close()


def select():
    '''
    根据学生的id和名字来查询学生信息
    '''''
    _id = ''
    _name = ''
    select_stu = []
    while True:
        # 判断文档是否存在
        if os.path.exists(file_location):
            check = input('根据id查询输入1，根据姓名查询请按2：')
            if check == '1':
                _id = input('请输入学生id')
            elif check == '2':
                _name = input('请输入学生姓名')
            else:
                print('您的输入有误')
                select()
            # 以只读的形式来打开文件
            with open(file_location, mode='r', encoding='utf-8') as r_file:
                l_stu = r_file.readlines()  # []
                for item in l_stu:  # item : {} {} {}
                    item = dict(eval(item))
                    if _id:
                        if item['id'] == _id:
                            select_stu.append(item)
                    elif _name:
                        if item['name'] == _name:
                            select_stu.append(item)
        # 显示查询结果
        show_all(select_stu)
        # else:
        select_stu.clear()
        # 询问是否继续查询
        choice = input('继续查询请按y/n')
        if choice == 'y':
            select()
        else:
            print('退出查询系统')
            break
        break


def show_all(lst):
    # 显示找到的结果
    # print(type(lst))
    if len(lst) == 0:
        print('当前这个文档中没有数据！！')
    # 定义好了输出的格式
    format_title = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    print(format_title.format('id', '姓名', 'c成绩', 'python', 'static', '总成绩'))
    # 定义内容格式
    format_data = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    for item in lst:  # id   name  ---  {}
        # print(type(lst))
        print(format_data.format(
            item.get('id'),
            item.get('name'),
            item.get('c'),
            item.get('python'),
            item.get('static'),
            int(item.get('c')) + int(item.get('python')) + int(item.get('static'))  # 统计总成绩
        ))


def delete():
    '''
    根据学生的id信息来删除学员
    :return:
    '''
    while True:
        stu_id = input('请输入要删除的学生id')
        if stu_id:
            # 读当前文件中的所有的学生信息
            with open(file_location, mode='r', encoding='utf-8') as r_file:
                # 读
                lst_stu = r_file.readlines()
            if lst_stu:
                with open(file_location, mode='w', encoding='utf-8') as w_file:
                    # 利用w的属性 删除用户选择的 学生id；
                    for item in lst_stu:  # [{},{},{}]
                        d = dict(eval(item))
                        if d['id'] == stu_id:
                            flag = 1    # 标记 学生信息删除成功
                        elif d['id'] != stu_id:
                            # 保留之前的所有数据
                            w_file.write(str(item))
                if flag == 1:
                    print('id为%s该学生信息删除成功' % stu_id)
                else:
                    print('没有找到id为%s学生信息' % stu_id)
                choice = input('还需要继续删除吗y/n')
                if choice == 'y':
                    delete()
                else:
                    print('退出删除系统')
                    break
            else:
                print('没有该学生信息')
        else:
            print('请输入要删除的学生id')
            delete()


def update():
    # 根据id进行修改
    if os.path.exists(file_location):
        _id = input('请输入要修改的学生id')
        if _id != '':
            # 读文件
            with open(file_location, 'r', encoding='utf-8') as r_file:
                lst = r_file.readlines()
                # 修改就是利用写的过程
                with open(file_location, 'w', encoding='utf-8') as w_file:
                    for item in lst:
                        d = dict(eval(item))
                        if d['id'] == _id:
                            print('请对学生信息进行修改！')
                            while True:
                                try:
                                    # 利用try''捕获异常
                                    d['name'] = input('请输入要修改的学生姓名:')
                                    d['c'] = int(input('请输入要修改的学生c:'))
                                    d['python'] = int(input('请输入要修改的学生python:'))
                                    d['static'] = int(input('请输入要修改的学生html:'))
                                except:
                                    print('成绩只能是数字！')
                                else:
                                    break
                            w_file.write(str(d) + '\n')
                        else:
                            # 将原来的数据添加进去
                            w_file.write(str(d) + '\n')
            # 询问是否要继续修改
            chioce = input('是否继续y/n')
            if chioce == 'y':
                update()
            else:
                print('退出修改~')
        else:
            print('请输入学生的id')
            update()
    else:
        print('没有学生文件')
    pass


def sort():
    lst_new = []
    flag = True  # 默认降序
    # 判断这个文件夹是否存在
    if os.path.exists(file_location):

        # 如果文件存在拿出里面的数据，
        with open(file_location, 'r', encoding='utf-8') as r_file:
            lst = r_file.readlines()

            for item in lst:
                d = dict(eval(item))
                lst_new.append(d)
            # 将转换成字典的lst_new这个传递到show_all里面
            show_all(lst_new)
        # 实现排序的功能！
        check = input('升序1/降序2:')
        if check == '1':
            flag = False
        elif check == '2':
            flag = True
        choice = int(input('c：输入1,python:输入2,static:输入3,总成绩:输入4：'))
        if choice == 1:
            # 来实现排序效果
            lst_new.sort(key=lambda x: int(x['c']), reverse=flag)
        elif choice == 2:
            lst_new.sort(key=lambda x: int(x['python']), reverse=flag)
        elif choice == 3:
            lst_new.sort(key=lambda x: int(x['static']), reverse=flag)
        elif choice == 4:
            lst_new.sort(key=lambda x: (int(x['c']) + int(x['python']) + int(x['static'])), reverse=flag)
        else:
            print('请输入正确的编号！')
            sort()
        # 排序完毕之后
        show_all(lst_new)
    else:
        print('没有这个文件')
        return


def alls():
    # 显示所有的学生信息
    l = []
    if os.path.exists(file_location):
        with open(file_location, 'r', encoding='utf-8') as r_file:
            lst = r_file.readlines()
            print('总共有%d数据' % len(lst))
            for item in lst:
                d = dict(eval(item))
                l.append(d)
            show_all(l)
    else:
        print('当前文件不存在！')


if __name__ == '__main__':
    mains()
