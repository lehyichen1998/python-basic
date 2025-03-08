'''

'''

import os

db_file = 'stu_database.txt'


def menu():
    print('================', '学生管理系统', '===========')
    print('================', '功能菜单', '================')
    print('                 1:输入学生信息              ')
    print('                 2:查找学生信息              ')
    print('                 3:删除学生信息              ')
    print('                 4:修改学生信息              ')
    print('                 5:排序学生信息              ')
    print('                 6:显示所有学生信息           ')
    print('                 0:退出当前系统              ')
    print('===========================================')


def add():
    stu_data = []
    global c, python, html
    print('这是add函数！！！！')
    while True:
        stu_id = input('请输入学生id: ')
        if not stu_id:
            break
        stu_name = input('请输入学生姓名: ')
        if not stu_name:
            break
        try:
            c = int(input('请输入学生c语言成绩: '))
            python = int(input('请输入学生Python语言成绩: '))
            html = int(input('请输入学生html语言成绩: '))
        except Exception:
            print('请用整数输入!!!')
        stu_dc_data = {'id': stu_id, 'name': stu_name, 'c': c, 'python': python, 'html': html}
        stu_data.append(stu_dc_data)
        check = input('还要继续添加吗???(y/n)')
        if check.lower() == 'y':
            add()
        else:
            print('完成添加, 离开添加操作!!!')
        save(stu_data)
        # print(stu_data)
        break


def save(lst_data):
    try:
        # a is add data
        stu_w_txt = open(db_file, mode='a', encoding='utf-8')
    except:
        # w is add data
        stu_w_txt = open(db_file, mode='w', encoding='utf-8')
    for i in lst_data:
        stu_w_txt.write(str(i) + '\n')
    stu_w_txt.close()


def show_all(lst):
    if len(lst) == 0:
        print('当前文档没有任何数据!!!')
    # format_title = '{:^10}\t{:^20}\t{:^30}\t{:^6}\t{:^6}\t{:^6}\t'
    # print(format_title.format('id', '姓名', 'c成绩', 'python', 'html', '总成绩'))
    format_data = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    for dc in lst:
        dc = dict(dc)
        print(
            format_data.format(
                dc.get('id'),
                dc.get('name'),
                dc.get('c'),
                dc.get('python'),
                dc.get('html'),
                int(dc.get('c')) + int(dc.get('python')) + int(dc.get('html')),
            )
        )


def select():
    stu_id = ''
    stu_name = ''
    query_lst = []
    while True:
        # alt+enter -->auto import module
        if os.path.exists(db_file):
            check = input('根据id输入1，根据name输入2:')
            if check == '1':
                stu_id = input('请输入要查询的学生id: ')
            elif check == '2':
                stu_name = input('请输入要查询的学生name: ')
            else:
                print('您的输入有吴，请输入1，或者2!!!!!!!!!!!!')
                select()
            with open(db_file, 'r', encoding='utf-8') as r_file:
                stu_lst = r_file.readlines()
                for i in stu_lst:
                    item = dict(eval(i))
                    if stu_id:
                        if item['id'] == stu_id:
                            query_lst.append(item)
                    elif stu_name:
                        if item['name'] == stu_name:
                            query_lst.append(item)
            show_all(query_lst)
            query_lst.clear()
            choice = input('还要继续添加吗???(y/n)')
            if choice.lower() == 'y':
                select()
            else:
                print('离开查询操作!!!')
            break
        else:
            print('请先添加学生信息!!!')
            add()


def delete():
    while True:
        stu_id = input('请输入要删除的学生id: ')
        if stu_id:
            with open(db_file, 'r', encoding='utf-8')as r_file:
                stu_lst = r_file.readlines()
            if stu_lst:
                with open(db_file, 'w', encoding='utf-8')as w_file:
                    for dc in stu_lst:
                        dc = dict(eval(dc))
                        if dc['id'] == stu_id:
                            flag = True
                        if dc['id'] != stu_id:
                            w_file.write(str(dc))
                if flag == True:
                    print('id为%s 的学生信息删除成功' % stu_id)
                elif flag == None:
                    print('没找到%s 的学生信息' % stu_id)

                choice = input('是否继续删除呢？(y/n)')
                if choice.lower() == 'y':
                    delete()
                else:
                    print('退出删除模块!!!')
                    break
                break
            else:
                print('没有任何数据')

        else:
            print('请输入要删除的学生id: ')
            delete()


def update():
    if os.path.exists(db_file):
        stu_id = input('请输入要修改的学生id: ')
        if stu_id != '':
            with open(db_file, mode='r', encoding='utf-8') as r_file:
                lst_data = r_file.readlines()
                if lst_data:
                    with open(db_file, mode='w', encoding='utf-8') as w_file:
                        for item in lst_data:
                            item = dict(eval(item))
                            if item['id'] == stu_id:
                                print('请对该学生%s信息进行修改' % item['name'])
                                while True:
                                    try:
                                        item['name'] = input('请输入您修改的学生姓名: ')
                                        item['c'] = int(input('请输入您修改的学生c成绩: '))
                                        item['python'] = int(input('请输入您修改的学生python成绩: '))
                                        item['html'] = int(input('请输入您修改的学生html成绩: '))
                                    except:
                                        print('成绩只能是整数!!!')
                                    else:
                                        break
                                w_file.write(str(item) + '\n')
                            else:
                                w_file.write(str(item) + '\n')
                else:
                    print('当前没有数据!!!')
            choice = input('是否继续修改?(y/n)')

    else:
        print('当前文档不存在!!!')


def sort():
    sign = True
    new_list = []
    if os.path.exists(db_file):
        with open(db_file, mode='r', encoding='utf-8') as r_file:
            lst = r_file.readlines()
            for i in lst:
                i = dict(eval(i))
                new_list.append(i)
            show_all(new_list)
        check = input('升序1，降序2: ')
        if check == '1':
            sign = False
        elif check == '2':
            sign = True
        choice = input('请输入排序的序号: C:1,HTML:2,Python:3,total:4 ')
        if choice == '1':
            new_list.sort(key=lambda x: int(x['c']), reverse=sign)
        elif choice == '2':
            new_list.sort(key=lambda x: int(x['html']), reverse=sign)
        elif choice == '3':
            new_list.sort(key=lambda x: int(x['python']), reverse=sign)
        elif choice == '4':
            new_list.sort(key=lambda x: int(x['c']) + int(x['html']) + int(x['python']), reverse=sign)
        else:
            print('请输入正确信息')
            sort()
        show_all(new_list)
    else:
        print('文件不存在!!!')


def all():
    l = []
    if os.path.exists(db_file):
        with open(db_file, mode='r', encoding='utf-8')as r_file:
            lst = r_file.readlines()
            print('一共有%d数据')
            for i in lst:
                i = dict(eval(i))
                l.append(i)
            show_all(l)

    else:
        print('没有此文件!!!')
        check = input('需要添加数据吗?(y/n)')
        if check.lower() == 'y':
            add()
        else:
            print('回到主函数!!!')


def mains():
    while True:
        menu()
        user_check = int(input('请输入您要执行的操作序号: '))
        if user_check in [0, 1, 2, 3, 4, 5, 6]:
            if user_check == 0:
                check = input('您真的要退出系统?(y/n)')
                if check.lower() == 'y':
                    print('退出当前系统,欢迎下次使用~')
                    break
                elif check.lower() != 'y' or check.lower() != 'n':
                    print('请选择y或n~')
            elif user_check == 1:
                add()
            elif user_check == 2:
                select()
            elif user_check == 3:
                delete()
            elif user_check == 4:
                update()
            elif user_check == 5:
                sort()
            elif user_check == 6:
                all()


if __name__ == '__main__':
    mains()
