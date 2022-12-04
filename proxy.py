
import requests
import multiprocessing
from bs4 import BeautifulSoup


def handler(proxy):
    link = 'https://icanhazip.com/'
    proxies = {
        'http': f'http//{proxy}',
        'https': f'http//{proxy}'
    }

    try:

        responce = requests.get(link, proxies=proxies, timeout=2).text
        print(f' IP: {responce.strip()}')
    except:
        print('Proxy is invalid')

with open('proxy.txt') as f:
    proxy_base = f.readlines()

if __name__ == '__main__':
    with multiprocessing.Pool(processes=8) as process:
        process.map(handler, proxy_base)
    


