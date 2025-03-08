import datetime as tm
data = '2021-04-14'


# 将页面传递来的 str字符 日期 转成 对应的日期数
#获取当前日期格式，将字符类型转换成时间类型，将数据进行格式
days = tm.datetime.strptime(data, '%Y-%m-%d')
print(days,type(days))
d = days.weekday() # 通过weekday来获取时间的索引
print(d)
# 定义格式化日期， 如果索引为1 就将其转化为周一；一次类推
week_day = {
    1: '周一',
    2: '周二',
    3: '周三',
    4: '周四',
    5: '周五',
    6: '周六',
    7: '周天'
}

print(week_day[d])