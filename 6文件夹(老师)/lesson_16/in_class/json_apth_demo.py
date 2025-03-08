'''
课堂演示目标网址：
http://www.lagou.com/lbs/getAllCitySearchLabels.json

使用jsonpath对目标网址进行信息提取；
    本节课的内容：
        基于jsonpath实现信息的提取；

'''

import requests
import json
# 如果没有该模块 ，直接pip 下载，pip 下载不了 去csdn 找相关的博客：download
import jsonpath as js


url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}
repones = requests.get(url,headers=head)

json_data = repones.text
# print(json_data)
# jsonpath,还可以用正则表达式：不记它，只有当使用到的时候才用正则表达式
dc_data = json.loads(json_data)

# json_path提取里面的关键字 城市名称，城市的id
city_name = js.jsonpath(dc_data,'$..name')
city_id = js.jsonpath(dc_data,'$..id')


print(city_name)
print(city_id)