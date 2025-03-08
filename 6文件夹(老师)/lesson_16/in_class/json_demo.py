# 将台服的英雄数据保存到 txt文档.文档的名字命名为 英雄.json结尾

# 向目标地址发送请求获得数据响应
import requests
import json
url = 'https://ddragon.leagueoflegends.com/cdn/11.6.1/data/zh_TW/champion.json'

#
head = {
    # request headers: 请求的头部信息；
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
# print(type(head))
respones = requests.get(url,headers=head)
json_data = respones.text

# print(json_data)


# 将数据进行取舍  name，id，title，blurb
dc_data = json.loads(json_data)
data = dc_data['data']

# 新建一个列表保存所有的数据
        # lst_data = []
        # for i in data:
        #     print(i)
        #     lst_data.append(i)

        # print(len(lst_data))

# 通过英雄的title取里面的value
lst_data = []
for sname in data:
    name = data[sname]['name']    # sname:厄薩斯
    id = data[sname]['id']
    title = data[sname]['title']
    blurb = data[sname]['blurb']
    lst = [name,id,title,blurb]
    lst_data.extend(lst)
    print(lst)


# 保存英雄数据
with open('lol_hero_data.txt','w',encoding='utf-8') as w_hero:
    for i in lst_data:
        w_hero.write('\n')
        for j in i:
            w_hero.write(j)

