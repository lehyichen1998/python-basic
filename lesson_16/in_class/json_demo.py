import requests
import json

# go champion.json get (network then f5)
url = 'https://ddragon.leagueoflegends.com/cdn/11.6.1/data/zh_TW/champion.json'
head = {
# go champion.json get (network then f5)
    'Referer': 'https://lol.garena.tw/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
response = requests.get(url, headers=head)
json_data = response.text
# print(json_data)

dc_data = json.loads(json_data)
data = dc_data['data']

# lst_data = []
# for i in data:
#     print(i)
#     lst_data.append(i)
#
# print(len(lst_data))

lst_data = []
for title_name in data:
    name = data[title_name]['name']
    id = data[title_name]['id']
    title = data[title_name]['title']
    blurb = data[title_name]['blurb']
    lst = [name, id, title, blurb]
    lst_data.extend(lst)
    print(lst)

with open('lol_hero_data.txt', 'w', encoding='utf-8') as w_hero:
    for i in lst_data:
        w_hero.write('\n')
        for j in i:
            w_hero.write(j)
