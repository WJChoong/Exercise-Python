import requests

payload = {"key1": "value1", "key2": "value2"} #设定好资料
r = requests.post("http://httpbin.org/post", data = payload)  #放入资料
print(r.text)

'''
print("-"* 100)
print("以下为原版")
r = requests.post("http://httpbin.org/post")
print(r.text)
'''
'''
r = requests.post("http://httpbin.org/post", data = "ABC")  #放入资料
print(r.text)
'''

r = requests.put("http://httpbin.org/put", data = payload)  #放入资料
print(r.text)