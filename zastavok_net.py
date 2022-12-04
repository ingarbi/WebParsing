import requests
from bs4 import BeautifulSoup
import fake_useragent
session = requests.Session()

storage_number = 1
image_number = 0
link = f'https://zastavok.net'

for storage in range(1):

    responce = requests.get(f'{link}/{storage_number}').text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', class_ = 'block-photo')
    all_image = block.find_all('div', class_ = 'short_full')

    for image in all_image:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}{image_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = download_soup.find('div', class_ = 'image_data').find('div', class_ = 'block_down')
        result_link = download_block.find('a').get('href')
        # print(result_link)
        # print(image_link)

        image_bytes = requests.get(f'{link}{result_link}').content


        with open(f'images/{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)

        image_number += 1
        print(f'Image downloaded {image_number}')
    storage_number += 1