import requests
from bs4 import BeautifulSoup
import re

def get_img_urls(soup):
    """ Generates a list of strings with the URL's of the images """
    images = soup.find_all('img')
    links = [image['src'] for image in images]
    return links

def get_chapters_urls(chapter_url:str, n:int):
    """ Generates a list of urls
    EXAMPLE URL: 'dorohedoro.online/manga/dorohedoro-chapter-[1]/'
    """
    urls = list()
    for i in range(n):
        urls.append(re.sub("\[[^]]*\]", lambda x: str(i), chapter_url))
    return urls


def imageDownload(images_links):
    for i, link in enumerate(images_links):
        if (link.startswith("https://")):
            with open('.png','wb') as f:
                im = requests.get(link)
                f.write(im.content)
