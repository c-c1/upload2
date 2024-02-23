from time import sleep
from instagrapi import Client
from termcolor import colored
import pyfiglet
import os
import ssl
import random
import requests
from bs4 import BeautifulSoup
import re

ssl._create_default_https_context = ssl._create_unverified_context

client = Client()
font = pyfiglet.figlet_format("instagram Tools", font="slant")
list_color = ['green', 'blue', 'cyan', 'yellow']

rand_color = random.choice(list_color)
rand_color2 = random.choice(list_color)

print(colored(font, rand_color))
print(colored('----------------------------------------------------', rand_color2))

username_my = input(colored('user::>  ', 'green'))
password = input(colored('pass::>  ', 'green'))
paths = (username_my + '.json')

try:
    if os.path.exists(paths):
        client.load_settings(paths)
        client.login(username_my, password)
        print(colored('\nLOGING DONE', "magenta"))
    else:
        client.login(username_my, password)
        client.dump_settings(paths)
        print(colored('\nDONE SAVE', 'green'))
except Exception as e:
    print(colored(f'\nError: {e}', 'red'))
    exit()

def extract_image_urls(page_url):
    response = requests.get(page_url)
    
    if response.status_code != 200:
        print(f"فشل في جلب الصفحة. الرمز الاستجابة: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    image_urls = []
    for img_tag in img_tags:
        src = img_tag.get('src')
        if src and re.search(r'_low\.webp$', src):
            image_urls.append(src)
    
    return image_urls

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"done save {save_path}")
        return [save_path] 
    else:
        print(f"error {response.status_code}")
        return []

def upload(path):
    try:
        # nump = input('numper: ')
        # if nump == '1':
            client.photo_upload_to_story(path)
            print('DONE UPLOAD STORY')

        # elif nump == '2': لنشر صورة عام
        #     client.photo_upload(path,'photo')
        #     print('DONE UPLOAD POST')
    except Exception as e:
        print(f'ERROR UPLOAD STORY: {e}')

# بنية منفردة
# https://www.seaart.ai/ar/explore/detail/ckb4a014msb0ko3kvl2g
        
# girl 
# https://www.seaart.ai/ar/searchView?keyword=girl
        
# cat
# https://www.seaart.ai/ar/models/detail/76176ff16ca482cd35c591dd9046dbe7
# kali linux
# https://www.seaart.ai/ar/explore/detail/cjpe0694msb0qs126sh0
page_url = "https://www.seaart.ai/ar/explore/detail/cjpe0694msb0qs126sh0"
#https://www.seaart.ai/ar/searchView?keyword=programming
image_urls = extract_image_urls(page_url)


selected_image_url = random.choice(image_urls)


save_path = "downloaded_image.jpg" 
print(f"done download photo {selected_image_url}")


rand = download_image(selected_image_url, save_path)
dawn = random.choice(rand)
upload(dawn)


for _ in range(4):
   
    selected_image_url = random.choice(image_urls)

    
    save_path = "downloaded_image.jpg" 
    print(f"done download photo {selected_image_url}")

    rand = download_image(selected_image_url, save_path)
    dawn = random.choice(rand)
    upload(dawn)
    os.remove(save_path)
    sleep(25)

