import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random

header = {'user-agent' : user}

link = 'https://browser-info.ru/'
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'lxml')


block = soup.find('div', id = 'tool_padding')

check_js = block.find('div', id = 'javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'javascripts : {status_js}'

check_flash = block.find('div', id = 'flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash {status_flash}'

check_user = block.find('div', id = 'user_agent').text

print(check_user)