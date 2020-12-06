import requests

r = requests.head('http://httpbin.org/get')
print(r.headers)    # 获取头部信息
print(r.text)      #无内容