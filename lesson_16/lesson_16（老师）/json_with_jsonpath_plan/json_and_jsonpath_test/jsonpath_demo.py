'''
课堂演示目标网址：
http://www.lagou.com/lbs/getAllCitySearchLabels.json

使用jsonpath对目标网址进行信息提取；
    本节课的内容：
        基于jsonpath实现信息的提取；

'''

import requests
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
response = requests.get(url, headers=header)

json_data = response.text

# 把json格式字符串转换成python的字典对象
dc_data = json.loads(json_data)
# print(dc_data)
# 从根节点开始，匹配name节点
city_list_name = jsonpath.jsonpath(dc_data, '$..name')
city_list_id = jsonpath.jsonpath(dc_data, '$..id')

# 查看city_list_name的数据
print ('citylist_name',city_list_name)
    # print('city_list_id', city_list_id)
# 查看city_list_name 和 city_list_id 的数据类型；
print('city_list_name', type(city_list_name), 'city_list_id', type(city_list_id))

# 将json的数据保存到 file中
with open('../city_json.txt', mode='w', encoding='utf-8') as w_json:
    for i in city_list_name:
        w_json.write(i + '\n')

content = json.dumps(city_list_name, ensure_ascii=False)  # ensure_ascii=False不使用ascii编码
print(type(content), content)

#  使用json直接进行转换；

# dc_content = dc_data['content']
# dc_data = dc_content['data']
# dc_all = dc_data['allCitySearchLabels']
# result = dc_all['A']

# 保存所有的城市数据
# city_data = []
# for item in dc_all:
#     for j in item:
#         result = dc_all[j]  # 根据每个城市得到的名字首字母
#     # city_data.append(result)
#         for k in result:
#             # 拿出里面面所有的字典数据
#             c_name = k['name']
#             city_data.append(c_name)
# print(city_data)
# print(len(city_data))
