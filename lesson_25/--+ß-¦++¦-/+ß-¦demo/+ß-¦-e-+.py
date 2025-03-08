import os
def start( ):   #  开始的输入提示  和按键提示
    print('\t'+'\t'+'\t'+'欢迎使用出行时间估算系统 :)')
    print('\n'*2)
    print('\t'+'\t'+'\t'+'1 - 开始模拟')

    print('\n')
    print('\t'+'\t'+'\t'+'0 - 结束程序')
    while True:
        put=input('请输入你的选择 >>')
        if put not in ['1','0']:
            print('选择无效，请重新键入(0 - 1)')
        else:
            return put
def staring_input():   #  判断输入开始地址是否正确
    while True:
        starting=input('请选择您的起始位置 >> ')
        if starting not in ['1','2','3','4','5']:
            print('请再输入一次')
        else:
            return starting
def destination_input(): #判断结束地址是否正确
    while True:
              destination=input('请择您的目的地位置 >> ')
              if destination not in ['1', '2', '3', '4', '5', '6']:
                  print('请再输入一次')
              else:
                 return destination
def Bike(distancing):  # 自行车的时间计算
    distancing = float(distancing)
    bike = 15.0
    bike_time = distancing / bike
    if bike_time * 60 >= 60:
        h = int(bike_time)
        m = (bike_time - h) * 60
        return h, m
    else:
        h=0
        m=bike_time*60
        return h,m
def Bus(distancing):    # 公交车的时间计算
    distancing = float(distancing)
    bus = 50.0
    bus_time = distancing / bus
    if bus_time*60>=60:
        h=int(bus_time)
        m=(bus_time-h)*60
        return h,m
    else:
        h=0
        m=bus_time*60
        return h,m
def  Taxi(distancing): # 的士的时间计算
    distancing = float(distancing)
    taxi = 70.0
    taxi_time = distancing / taxi
    if taxi_time * 60 >= 60:
        h = int(taxi_time)
        m = (taxi_time - h) * 60
        return h, m
    else:
        h=0
        m=taxi_time*60
        return h,m
def Walk(distancing): # 步行的时间计算
    distancing = float(distancing)
    walk = 5.0
    walk_time = distancing / walk
    if walk_time * 60 >= 60:
        h = int(walk_time)
        m = (walk_time - h) * 60
        return h, m
    else:
        h=0
        m=walk_time*60
        return h,m
def Transportation():  #选择交通方式
    os.system('cls')  #清除所有已经显示的信息
    print('1.bike')
    print('2.bus')
    print('3.taxi')
    print('4.walk')
    transportation=input('请选择您的出行方式 >>')
    while True:
        if transportation in ['1', '2', '3', '4']:
            if  transportation=='1':
                return 'bike'
            elif transportation=='2':
                return 'bus'
            elif transportation=='3':
                return 'taxi'
            else:
                return 'walk'
        else:
            print('请再输入一次')
def distance(transportation,distancing):
    # 判断交通方式并且返回对应的计算时间 配合上面的时间计算
    if transportation == 'bike':
        return Bike(distancing)
    elif transportation == 'bus':
        return Bus(distancing)
    elif transportation == 'walk':
        return Walk(distancing)
    else:
        return Taxi(distancing)
def end_print(start,destination,distancing,transportation,h1,m1):
    # 选择完交通方式后打印对应的值
    os.system('cls')
    print('开始位置     :{}'.format(start))
    print('目标位置  :{}'.format(destination))
    print('\n')
    print('距离              :{} KM'.format(distancing))
    print('你使用的交通工具 :{}'.format(transportation))
    print('估计旅行时间 :{} 小时 {} 分钟'.format(h1,m1))
    input('按enter继续')
def position():
    #选择相应的距离并且提示
    print('1 - 帝国大厦')
    print('2 - 纽约时代广场')
    print('3 - 自由女神像')
    print('4 - 纽约中央公园')
    print('5 - 9/11纪念馆')
    starting=staring_input()   #通过判断开始地址函数来确定输入是否正确
    destination=destination_input()  #通过判断结束地址函数来确定输入是否正确
    starting=int(starting)   #将输入的值转换为int类型
    destination=int(destination)   #将输入的值转换为int类型
    if starting==1 or destination==1:  #判断输入的值中是否有  1
        if destination==starting :   #判断两个输入值是一样的
            distancing=0    #两个位置之间的距离
            transportation=Transportation()   #实例化交通工具函数
            h,m=distance(transportation,distancing)
            # 将交通工具函数 和距离导入到计算时间函数
            end_print(starting,destination,distancing,transportation,h,m)
            #  打印最后的结果
        elif destination==2 or starting==2:  #判断两个输入值中有没有  2
            #（1,2）或者（2,1）的距离
            distancing=1.8   #两个位置之间的距离
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
        elif destination == 3 or starting == 3:
            #（1,3）或者（3,1）的距离
            distancing=8.3   #两个位置之间的距离
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
        elif destination == 4 or starting == 4:
            distancing=3.2  #两个位置之间的距离
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
        elif destination == 5 or starting == 5:
            distancing=9.4
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
    elif starting == 2 or destination == 2:
        if destination==starting :
            distancing=0
            transportation=Transportation()
            h,m=distance(transportation,distancing)
            end_print(starting,destination,distancing,transportation,h,m)
        elif destination == 3 or starting == 3:
            distancing=9.8
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
        elif destination == 4 or starting == 4:
            distancing=9
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
        elif destination == 5 or starting == 5:
            distancing=6.2
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
    elif starting == 3 or destination == 3:
        if destination==starting :
            distancing=0
            transportation=Transportation()
            h,m=distance(transportation,distancing)
            end_print(starting,destination,distancing,transportation,h,m)
        elif destination == 4 or starting == 4:
            distancing = 9
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
        elif destination == 5 or starting == 5:
            distancing =2.3
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
    elif starting == 4 or destination == 4:
        if destination==starting :
            distancing=0
            transportation=Transportation()
            h,m=distance(transportation,distancing)
            end_print(starting,destination,distancing,transportation,h,m)
        elif destination == 5 or starting == 5:
            distancing =10.5
            transportation = Transportation()
            h, m = distance(transportation, distancing)
            end_print(starting, destination, distancing, transportation, h, m)
    else:
        if destination==starting :
            distancing=0
            transportation=Transportation()
            h,m=distance(transportation,distancing)
            end_print(starting,destination,distancing,transportation,h,m)
def User():   # 用户登录
    user=input('请输入用户名 >> ')
    password=input('请输入用户密码 >> ')
def main():
    #  程序的运维步骤
        User()
        while True:   #没有输入0就无限循环
            os.system('cls') #清除所有已经显示的信息
            a=start()   #拿到最初输入的值
            os.system('cls')  #清除所有已经显示的信息
            if a=='1':  # 判断最初输入的是否为1  如果是1 就执行下面的程序
                position()
            else:  #  如果不是1 那么只剩下 0   所以就终止程序
                return
main()


