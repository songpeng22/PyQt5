#导入请求包
import requests
#导入json包
import json
#
#设置要访问的地址（这里是get请求）
url = 'https://www.tianqiapi.com/api?version=epidemic&appid=23035354&appsecret=8YvlPNrz'
#直接请求
r = requests.get(url)
#这里是输出了一个字符串
#print(r.text)
#用自带的json工具把字符串转成字典
d = json.loads(r.text)
#输出字典
#print(d)
#用字典的方法获取值
print(d["errcode"])
#date
print(d["data"]["date"])
#new
print(d["data"]["diagnosedIncr"])
#list
print( "list:" )
print(d["data"]["list"])
list = d["data"]["list"]
print( "item in list:" )
for i in list:
    print( i )
#history
print( "history:" )
print(d["data"]["history"])
listOfHistory = d["data"]["history"]
print( "item in history:" )
for i in listOfHistory:
    print( i )
#area
print( "area:" )
print(d["data"]["area"])


#history
url = 'https://tianqiapi.com/api?version=epidemic_history&appid=&appsecret='
r = requests.get(url)
#用自带的json工具把字符串转成字典
d = json.loads(r.text)
list = d["data"]
for i in list:
    print( i )

