'''
Json:
    'javaScript Obuject notation'
    json是轻量级的文本数据交互格式
    json独立语言*
    json具有自我描述性，更易理解
    json比xml更小更快更易理解

'''
'''
什么是json？
    json的类型跟python中的字典长得非常的像但是又不是字典
    例“
        json格式：
        json_str = {"name":"小白","age":20,"like_learning":true,"massage":null}
        python字典格式：
        dict_str = {'name':'小白','age':20,'like_learning':True,'massage':none}
        
        json_str = {"name":"小白","age":20,"favorit":["python","basketball","run"]}
            
json在python中的常用方式：
    1.编码(encode)：把一个python对象编码转换成json字符串 json.dumps()
    2.解码(decode)：把json格式字符串解码转换成python对象 json.loadS()
    dumps()  domp是将 Python的数据类型转换为 json
    loads()  load是将 json数据转化为 json
'''
import json
#使用json.dump进行转化：
dict_str = {'name':'小白','age':20,'like_learning':True}
#输出当前的dict_str类型
print(type(dict_str))
#将字典类型转换为json格式，注意：json格式在python中不会以‘json’格式输出，而是str
is_josn = json.dumps(dict_str)
print(type(is_josn))

'''
    总结：json它就是一种数据格式，是一种网页间轻量级的数据传输模式，现在基本上都是用json
    #进行数据的传输，应为及轻快，等特性遍布在各大平台的网页中进行数据交互，
    #常用于聊天，页面文字的信息传输，
'''
