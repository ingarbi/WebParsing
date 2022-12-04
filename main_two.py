import requests
from bs4 import BeautifulSoup
import fake_useragent
session = requests.Session()




link = 'https://berkat.ru/auth/login'

user = fake_useragent.UserAgent().random

header = {'user-agent' : user}

data = {
    'auth_phone:': '+122312341',
    'password': '1231232320'
}

responce = session.post(link, data=data, headers=header).text

profile_info = 'https://berkat.ru/users/194967'
profile_responce = session.get(profile_info).text


cookies_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)


resp = session2.get(profile_info, headers=header)


print(resp.text)
