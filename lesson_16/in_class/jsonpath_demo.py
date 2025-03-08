import requests
import json
import jsonpath as js

# go champion.json get (network then f5)
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
head = {
    # go champion.json get (network then f5)
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

response = requests.get(url, headers=head)
json_data = response.text
dc_data = json.loads(json_data)

print(dc_data)

city_name = js.jsonpath(dc_data, '$..name')
city_id = js.jsonpath(dc_data, '$..id')

print(city_name)
print(city_id)
