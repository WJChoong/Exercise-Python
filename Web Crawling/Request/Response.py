import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
print(type(r))   #return type of r
print(r.headers) #return get to receive the header of the website

print(r.text) #读取网页
print(r.encoding) #从header中获取编码方式
print(r.apparent_encoding) #从内容分析编码方式

r.encoding = "utf-8"  #把编码方式换取另一个
print(r.text) #再次读取