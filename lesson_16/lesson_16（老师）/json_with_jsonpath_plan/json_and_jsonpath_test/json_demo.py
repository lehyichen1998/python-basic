'''
对台服英雄联盟的公开数据进行抓取：
    此地址为目标地址：
    https://lol.garena.tw/game/champion

'''
import json

import requests

url = 'https://ddragon.leagueoflegends.com/cdn/11.1.1/data/zh_TW/champion.json'
heaher = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

respones = requests.get(url,headers = heaher)

# print(respones.text)
result = respones.text
dc_result = json.loads(result)
# 将页面的数据进行转换
# for i in dc_result:
''' :type  format   verson   data'''
#     print(i) # 打印得到该json有主要以下key

lol_type = dc_result['type']
lol_format = dc_result['format']
lol_verson = dc_result['version']
lol_data = dc_result['data']

# 查看key中里面的所有值
# print(lol_data)
# print(lol_format)
# print(lol_verson)
# print(lol_type)
# 去data里面所有的数据

lst_lol = []
for i in lol_data:
    lst_lol.append(i)
    print(i)
print(len(lst_lol))

# 将json转换成字典对里面的数据进行提取
lol_hero = []
for lol_datas in lol_data:
    l_blurb = lol_data[lol_datas]['blurb']  # 英雄介绍
    l_name = lol_data[lol_datas]['name']  # 英雄名称
    l_tags = lol_data[lol_datas]['tags'][0:-1]  # 拿英雄的属性
    l_title = lol_data[lol_datas]['title']  # 英雄标题
    li = [l_blurb,l_name,l_tags,l_title]
    print(li)
    lol_hero.extend(li)

# 保存英雄数据
with open('英雄参数2.txt','w',encoding='utf-8',newline='') as w_hero:
    for i in lol_hero:
        w_hero.write('\n')
        for j in i:
            w_hero.write(j)



