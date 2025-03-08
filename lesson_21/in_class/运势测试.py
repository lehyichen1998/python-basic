from flask import Flask, request, render_template
import requests

luck_app = Flask(__name__)


@luck_app.route('/')
def data():
    consName = request.args.get('consName')
    types = request.args.get('types')
    print(consName, types)
    if consName is None and types is None:
        result = requests.get(
            'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=%E5%8F%8C%E9%B1%BC%E5%BA%A7&type=today')
        name = result.json()['name']
        color = result.json()['color']
        datetime = result.json()['datetime']
        summary = result.json()['summary']
        print('请求的星座名称: %s ,color: %s,datetime: %s,summary: %s' % (name, color, datetime, summary))
        return render_template('today.html', name=name, color=color, datetime=datetime, summary=summary)
    elif consName != '' and types == 'today':
        result = requests.get(
            'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=%s&type=%s'
            % (consName, types))
        name = result.json()['name']
        color = result.json()['color']
        datetime = result.json()['datetime']
        summary = result.json()['summary']
        return render_template('today.html', name=name, color=color, datetime=datetime, summary=summary)
    elif consName != '' and types == 'tomorrow':
        result = requests.get(
            'http://web.juhe.cn:8080/constellation/getAll?key=e4f70a414b69541546fbbf631c70737f&consName=%s&type=%s'
            % (consName, types))
        name = result.json()['name']
        color = result.json()['color']
        datetime = result.json()['datetime']
        summary = result.json()['summary']
        return render_template('today.html', name=name, color=color, datetime=datetime, summary=summary)


if __name__ == '__main__':
    luck_app.run()
