import requests 
from bs4 import BeautifulSoup 
from fake_useragent import UserAgent

city = "Delhi" 
search = "Weather in {}".format(city) 
user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
'Safari/537.36'

headers = { 'User-Agent': user_agent_desktop}

url = f"http://www.google.com/search?q={search}&aqs=chrome..69i57j0i10i433l2j0i10j0i10i433.2805j0j7&client=ms-android-xiaomi-rev1&sourceid=chrome-mobile&ie=UTF-8"
   
# Sending HTTP request 
print(UserAgent())

req = requests.get(url,headers=headers) 

  
# Pulling HTTP data from internet 

sor = BeautifulSoup(req.text,"html.parser")  

  
# Finding temperature in Celsius 

temp = sor

  

print(temp) 
