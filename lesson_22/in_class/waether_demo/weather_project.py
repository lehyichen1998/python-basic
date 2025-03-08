from flask import Flask, render_template, request
import requests
import datetime as time

url = 'http://apis.juhe.cn/simpleWeather/query?key=1067ae868025e24d898fba6e5555b75b&city=长沙'

index_html = 'index.html'
weather_app = Flask(__name__)


@weather_app.route('/')
def weather_data():
    global reason
    city = request.args.get('city_s')
    if city:
        response = requests.get(url.replace('长沙', city))
    else:
        response = requests.get(url)

    try:
        all_weather = response.json()['result']
        reason = response.json()['reason']
        error_code = response.json()['error_code']
        city = all_weather['city']
        future = all_weather['future']
        day1 = [future[0]]  # day1
        day2 = [future[1]]  # day2
        day3 = [future[2]]  # day3
        day4 = [future[3]]  # day4
        day5 = [future[4]]  # day5

    except Exception as err:
        return render_template('error_page.html', reason=reason)
    return render_template('weather_page.html', city=city,
                           day1=day1, day2=day2, day3=day3, day4=day4, day5=day5)


@weather_app.template_filter('weeks')
def filter_week(data):
    days = time.datetime.strptime(data, '%Y-%m-%d')
    index_days = days.weekday()
    week_day = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    return week_day[index_days]


if __name__ == '__main__':
    weather_app.run()
