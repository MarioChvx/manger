import requests
from bs4 import BeautifulSoup
import os

def imageDownload(url,folder):
   path = os.getcwd()
   os.mkdir(os.path.join(path, folder))
   os.chdir(os.path.join(path, folder))
   r = requests.get(url)
   soup = BeautifulSoup(r.text, 'html.parser')
   
   images = soup.find_all('img')
   
   for image in images:
      link = image['src']
      name = image['alt']
      if (link.startswith("https://")):
         with open(name + '.png','wb') as f:
            im = requests.get(link)
            f.write(im.content)
   os.chdir(path)

url='https://www4.mymangalist.org/chapter-shuumatsu-no-valkyrie-'
caps = range(6,62)

for cap in caps:
   imageDownload(url+str(cap),'Chapter'+str(cap))

