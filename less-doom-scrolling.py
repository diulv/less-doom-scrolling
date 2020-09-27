import requests
from bs4 import BeautifulSoup

url = 'https://twitter.com/login'
username = "danielclaywillmott@gmail.com"
password = 'password'


r = requests.get('https://twitter.com/login')
soup = BeautifulSoup(r.content, "lxml")
token = soup.select_one("input[name=authenticity_token]")["value"]
params = {"session[username_or_email]": username,
        "session[password]": password,
		"authenticity_token": token}
r = s.post(url, data=params)
print(r.content)







#r = requests.get('https://twitter.com/settings/applications')