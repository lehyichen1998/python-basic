import datetime as time

data = '2021-04-14'

days = time.datetime.strptime(data, '%Y-%m-%d')
print(days)

index_week = days.weekday()
print(index_week)

week_day = {
    0: '周一',
    1: '周二',
    2: '周三',
    3: '周四',
    4: '周五',
    5: '周六',
    6: '周日',
}

print(week_day[index_week])