'''
学生管理系统：
    对学生信息进行增删改查
'''
# 数据库文档
import os

db_file = 'stu_database.txt'


# 选择序号

def menu():
    print('================ 学生管理系统 ==============')
    print('================ 功能菜单 ================')
    print('             1:录入学生信息     ')
    print('             2:查找学生信息 ')
    print('             3:删除学生信息  ')
    print('             4:修改学生信息')
    print('             5:排序学生信息  ')
    print('             6:显示所有学生信息 ')
    print('             0:退出当前系')
    print('=======================================')


# 功能函数：
def add():
    # 声明列表保存原有的字典数据
    stu_data = []
    global c, python, html  # 将变量引用成全局变量;
    while True:
        stu_id = input('请输入学生id:')
        if not stu_id:
            break
        stu_name = input('亲输入学生姓名:')
        if not stu_name:
            break
        # 添加学生成绩;
        try:
            #   以防用户输入信息错误；
            c = int(input('请输入学生的c语言成绩:'))
            python = int(input('请输入学生的python语言成绩:'))
            html = int(input('请输入学生的html语言成绩:'))
        except Exception:
            print('请用整数去定义学生成绩~')
        # 收集学生信息 ，将数据保存至 字典数据
        stu_dc_data = {'id': stu_id, 'name': stu_name, 'c': c, 'python': python, 'html': html}
        # 将以添加好的字典数据保存至列表中
        stu_data.append(stu_dc_data)  # [{},{},{}]
        # 询问是否继续操作；
        check = input('还要继续添加吗?(y/n):')
        if check == 'y' or check == 'Y':
            add()
        else:
            print('完成添加，离开添加操作~')
        # print(stu_data)
        save(stu_data)  # 1  ,  2
        break


# 定义save函数将数据 保存至 txt文档中；
def save(lst_data):  # [{"id":id......},{},{}]
    try:
        # a 表示追加 数据，但是不能创建文档，利用 w 创建文档的特性 为a 追加数据 做铺垫；
        stu_w_txt = open(db_file, mode='a', encoding='utf-8')
    except:
        # 用于第一次创建文档；
        stu_w_txt = open(db_file, mode='w', encoding='utf-8')
    for dc in lst_data:  # {}
        stu_w_txt.write(str(dc) + '\n')
    stu_w_txt.close()


# 此函数用于将数据进行格式化展示；
def show_all(lst):
    if len(lst) == 0:
        print('当前文档没有任何数据！！')
    # 定义标题的输出格式
    format_title = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    print(format_title.format('id', '姓名', 'c成绩', 'python', 'html', '总成绩'))
    # 定义内容输出格式
    # format_data = '{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t'
    for dc in lst:  # [{},{},{}]
        dc = dict(dc)
        print(
            format_title.format(
                dc.get('id'),
                dc.get('name'),
                dc.get('c'),
                dc.get('python'),
                dc.get('html'),
                # 所有分数的总和
                int(dc.get('c')) + int(dc.get('python')) + int(dc.get('html')),
            )
        )


def select():
    '''根据学生id和学生姓名进行持续查询'''
    # 将stu_id 和 stu_name整成全局变量,如果不将变量申明成全局变量的话 ，他就是局部变量，那么很有可能别的变量访问不到；
    global stu_id
    global stu_name
    # stu_id = ''
    # stu_name = ''
    query_lst = []  # 保存所有查询到的数据
    while True:
        # alt+ enter --->自动导包（module），
        if os.path.exists(db_file):
            check = input('根据id输入1，根据name输入2:')
            if check == '1':
                stu_id = input('请输入要查询的学生id:')
            elif check == '2':
                stu_name = input('请输入要查询的学生name:')
            else:
                print('您的输入有误,请输入1，或者2~')
                select()
            # 我得有 所有的数据，才能和 用户输入的 数据进行匹配
            with open(db_file, 'r', encoding='utf-8') as r_file:
                stu_lst = r_file.readlines()  # 一行[{},{},{}]
                for item in stu_lst:  # item --》 str -- > dict
                    # 将用户和db.txt里面的数据进行匹配,先强转成dict
                    item = dict(eval(item))
                    if stu_id:  # True
                        if item['id'] == stu_id:
                            query_lst.append(item)
                    elif stu_name:
                        if item['name'] == stu_name:
                            query_lst.append(item)
                    else:
                        print('您输入的id或者name 没有任何数据')
            # 当后端匹配到了和用户输入的信息一致时，我们将数据展现出来
            show_all(query_lst)
            # 为了数据匹配性，将原数进行清空
            query_lst.clear()
            # 询问是否继续查询
            choice = input('是否继续查询?(y/n):')
            if choice == 'y' or choice == 'Y':
                select()
            else:
                print('退出查询系统~')
                break
            break
        else:
            print('请先添加学生信息！')
            add()


def delete():
    '''根据学生的id删除 好好的利用读写功能'''
    flag = None
    while True:
        stu_id = input('请输入要删除的学生id:')
        if stu_id:
            # 读数据
            with open(db_file, 'r', encoding='utf-8') as r_file:
                stu_lst = r_file.readlines()
            if stu_lst:
                with open(db_file, 'w', encoding='utf-8') as w_file:
                    # 利用写的过程将用户选择的数据删除掉
                    for dc in stu_lst:  # stu_lst :  [{},{},{}]  dc: 1,str: 2
                        dc = dict(eval(dc))
                        if dc['id'] == stu_id:
                            flag = True  # 只是用于标识此id已删除
                            # 此时表示用户输入的id 和 数据源中的id是一致的，不用去管它
                            # 表示用户输入的 值和 原有的数据 一致，我就不将该数据写回去
                        if dc['id'] != stu_id:
                            # 这些数据不需要删除，我就将数据重新写回去
                            w_file.write(str(dc) + '\n')
                if flag == True:
                    print('id为%s 的学生信息删除成功' % stu_id)
                elif flag == None:
                    print('没有找到id为%s的学生信息' % stu_id)
                # 继续询问是否删除
                choice = input('是否继续删除呢(y/n):')
                if choice == 'y' or choice == 'Y':
                    delete()
                else:
                    print('退出删除模块~')
                    break
                break
            else:
                print('没有任何数据')
        else:
            print('请输入要删除的学生id:')
            delete()


def update():
    # 根据id进行修改
    if os.path.exists(db_file):
        stu_id = input('请输入要修改的学生id:')
        if stu_id != '':
            # 读文件，修改文件中的数据
            with open(db_file,mode='r',encoding='utf-8') as r_file:
                lst_data = r_file.readlines()
                # 利用读和写的流修改文档中的数据
                if lst_data:
                    with open(db_file,mode='w',encoding='utf-8') as w_flie:
                        for item in lst_data:
                            item = dict(eval(item))  # {}
                            # 用户输入的id和 字典中原有的 id的value一致，我就进行修改操作
                            if item['id'] == stu_id:
                                print('请对该学生%s信息进行修改'% item['name'])
                                while True:
                                    try:
                                        item['name'] = input('请输入您修改的学生姓名:')
                                        item['c'] = int(input('请输入您修改的学生c成绩:'))
                                        item['python'] = int(input('请输入您修改的py成绩:'))
                                        item['html'] = int(input('请输入您修改的html成绩:'))
                                    except:
                                        print('成绩只能是整数！')
                                    else:
                                        break
                                # 修改完毕之后，将原来的数据重新写入进去
                                w_flie.write(str(item)+'\n')
                            else:
                                # 将和用户修改的id不一致的 信息添加进去；
                                w_flie.write(str(item)+'\n')
                else:
                    print('当前文档没有数据！')
           # 是否要继续修改？
            choice = input('是否继续修改?(y/n)')
            if choice == 'y' or choice == 'Y':
                update()
            else:
                print('退出修改~')
    else:
        print('当前文档不存在！！')


def sort():
    # 文件是否存在
    sign = True  # 设置默认排序
    new_list = []
    if os.path.exists(db_file):
        # 读数据
        with open(db_file,mode='r',encoding='utf-8') as r_file:
            lst =  r_file.readlines()
            for i in lst:
                i = dict(eval(i))
                new_list.append(i)
            # 显示整个数据
            show_all(new_list)
        # 实现排序功能
        check = input('升序1，降序2:')
        if check == '1':
            sign = False
        elif check == '2':
            sign = True
        choice = input('请输入排序的序号:  C:1,HTML:2,Python:3,总成绩:4:')
        if choice == '1':
            # 根据用户的选择进行排序
            new_list.sort(key=lambda dc:int(dc['c']),reverse=sign )
        elif choice == '2':
            new_list.sort(key=lambda dc:int(dc['html']),reverse=sign )
        elif choice == '3':
            new_list.sort(key=lambda dc:int(dc['python']),reverse=sign )
        elif choice == '4':
            new_list.sort(key=lambda dc:int(dc['c'])+int(dc['html'])+int(dc['python']),reverse=sign )
        else:
            print('请输入正确的编号~')
            sort()
        # 显示排序信息
        show_all(new_list)
    else:
        print('文件不存在~')


def all():
    # 判断文档
    l = []
    if os.path.exists(db_file):
        with open(db_file,mode='r',encoding='utf-8') as r_file:
            lst = r_file.readlines()
            print('一共有%d数据~')
            for i in lst:
                i = dict(eval(i))
                l.append(i)
            # 显示所有数据
            show_all(l)
    else:
        print('没有此文件！')
        check = input('需要添加数据吗？(y/n)')
        if check == 'y':
            add()
        else:
            print('回到主函数~')


# 编写主函数：
def mains():
    # 重复显示菜单，判断用户输入的序号是否ok，执行和调用子函数，
    while True:
        menu()
        user_check = int(input('请输入您要执行的操作序号:'))
        if user_check in (0, 1, 2, 3, 4, 5, 6):
            if user_check == 0:
                check = input('您真的要退出系统?(y/n):')
                if check == 'y' or check == 'Y':
                    print('退出当前系统，欢迎下次使用~')
                    break
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
        pass


if __name__ == '__main__':  # main 回车即可；
    mains()



# 将案例进行打包；exe

# 打开powershell
#
# pyinstaller -F 文件名


