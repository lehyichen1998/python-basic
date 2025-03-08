# 导入flask的包
from flask import Flask, request, render_template
import requests
import datetime

html_file = 'index2.html'    #w文件路径
error_local = 'error.html'   #错误页面的路径
# 接口请求地址
url = 'http://apis.juhe.cn/simpleWeather/query?key=1067ae868025e24d898fba6e5555b75b&city=%E9%95%BF%E6%B2%99'
# 调用Flask的方法来创建一个app
app = Flask(__name__, template_folder='templates')


# 路由
@app.route('/')
def weather():
    # 保存待会儿可能会页面会输入的城市名称
    city = request.args.get('city')    # 获取页面的传来的city变量
    # 如果输入
    if city:    #True
        respones = requests.get(url.replace('%E9%95%BF%E6%B2%99', city))  #根据条件查询
    else:     #False
        respones = requests.get(url)   #默认查询，查询城市为长沙
    # 因为容易报错：
    try:
        h_city = respones.json()["result"]['city']
        city_weather = respones.json()["result"]["future"]   #{‘city’:'长沙'}

        # 根据以上得到的规律
        day1 = [city_weather[0]]
        print('day1',day1,type(day1))
        #第二天
        day2 = [city_weather[1]]
        #第三天
        day3 = [city_weather[2]]
        #第四天
        day4 = [city_weather[3]]
        # 第五天
        day5 = [city_weather[4]]
    except Exception as error:
        return render_template(error_local)
    # 利用json可以将其转换为字符串的形式，将其转换成字典类型
    # 渲染模板render_template()<h1>天气预报</h1>
    return render_template(html_file, h_city=h_city,day1 = day1,day2 = day2,day3 = day3,day4 = day4,day5 =day5)  #

# 来一个星期几的过滤器
@app.template_filter('weeks')  # 括号内接收前端传来的数据如weeks
def we(data): # 2021-02-01
    days = datetime.datetime.strptime(data, '%Y-%m-%d')  #将数据进行格式
    d = days.weekday() # 0-6 ;
    week_day = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周天'
    }

    print(data,type(data))
    return week_day[d]

if __name__ == '__main__':
    app.run()
