# 导入模块

from flask import Flask,render_template,request
import requests
import datetime as time

# api的请求地址;
url = 'http://apis.juhe.cn/simpleWeather/query?key=1067ae868025e24d898fba6e5555b75b&city=长沙'

index_html = 'index.html'

# 创建flask对象

weather_app = Flask(__name__)

# 配置路由
@weather_app.route('/')
def weather_data():
    # 获取页面传递来的值
    city = request.args.get('city_s')
    # 如果当city存在的情况下
    if city:
        respones = requests.get(url.replace('长沙',city))
    else:
        respones = requests.get(url)
    # 默认访问
    # 异常处理
    global reason  # 全局变量名
    try:
        all_weather = respones.json()['result']
        reason =respones.json()['reason']  # "reason":"暂不支持该城市"
        city =  all_weather['city']
        futrue = all_weather['future']  # 是一个列表


        # 根据以上规律;
        day1 = [futrue[0]]  # 第一天 {"date":"2021-04-14", "temperature":"14/16℃",....}
        day2 = [futrue[1]]
        day3 = [futrue[2]]
        day4 = [futrue[3]]
        day5 = [futrue[4]]   # 第五天
    except:
        return render_template('erro_page.html',reason = reason)
    return render_template('weather_page.html',city=city,
                           day1=day1,day2=day2,day3=day3,day4=day4,day5=day5)

# 对数据进行过滤 : 接受页面的 weeks 将数据格式成自己需要的样子，将数据再返回到页面上;
@weather_app.template_filter('weeks')
def filter_week(data):
    days = time.datetime.strptime(data,'%Y-%m-%d')
    index_day = days.weekday()
    week_day = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周天',
    }
    return week_day[index_day]

# 开启flask服务

# main  alt+/
if __name__ == '__main__':
    weather_app.run()