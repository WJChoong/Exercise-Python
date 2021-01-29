import requests

class keywords():
    def params():
        kv = {'key1': 'value1', 'key2': 'value2'}
        r = requests.request('GET', "http://httpbin.org/get", params=kv) #把kv的参数增加到url当中， 'GET'会把参数显示在url上       
        print(r.url) 
    
    def data():
        kv = {'key1': 'value1', 'key2': 'value2'}
        r = requests.request('POST', "http://httpbin.org/get", data=kv) #把kv的参数增加到data对应的位置当中
        print(r.status_code)
        body = '主体内容'
        body = body.encode('utf-8')
        r = requests.request('POST', 'http://httpbin.org/get', data = body) #把字母串存储在上述对应的位置
        print(r.status_code)
    
    def json():
        kv = {'key1': 'value1'} #json格式的数据
        r = requests.request('POST', "http://httpbin.org/get", json=kv) #把kv的参数增加到json域上
    
    def headers():
        hd = {'user-agent': 'Chrome/10'} #模拟第十代chrome浏览器
        r = requests.request('POST', "http://httpbin.org/get", headers=hd) #把hd赋给header
        print(r.headers)        
        
    def files():
        fs = {'file': open('data.xls''rb')} #用open的方式打开文件，与file做相连
        r = requests.request('POST', 'http://python123.io/ws', files = fs)
        
    def timoeut():
        r = requests.request('GET', 'http://www.baidu.com', timeou=10) #在限定时间没返回资源就会产生一场
        
    def proxies():
        pxs = { 'http': 'http://user:pass@10.10.10,1:1234', 
                'https': 'https://10.10.10.1:4321'} # 两个代理
        r = requests.request('GET', 'http://www.baidu.com', proxies = pxs)
        
choice = input("Enter your choice: ")
if choice == "1":
    keywords.params()
elif choice == "2":
    keywords.data()
elif choice == "3":
    keywords.json()
elif choice == "4":
    keywords.headers()
elif choice == "5":
    keywords.files()
elif choice == "6":
    keywords.timoeut()
elif choice == "7":
    keywords.proxies()