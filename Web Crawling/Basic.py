import requests 

# test connections
r = requests.get("https://www.google.com/")
print(r.status_code) #if status_code = 200 means success

r.encoding = "utf-8"
print(r.text)
