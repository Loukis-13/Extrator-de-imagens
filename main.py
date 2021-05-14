import urllib.request, urllib.parse, urllib.error
import requests
import os
from bs4 import BeautifulSoup

url = 'https://loukis-13.github.io/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, 'html.parser')

folder=url.replace('/', '-')
if not os.path.isdir(folder): os.makedirs(folder)

tags = soup('img')
for tag in tags:
    src = tag.get('src', None)
    print(src)

    if 'https://' in src or 'http://' in src:
        response = requests.get(src)
    else:
        if '/' != src[0]:
            src = '/'+src
        response = requests.get(req.type + '://' + req.host + src)

    file_name = src.split('/')[-1].split('?')[0]
    with open(folder + "/" + file_name, "wb") as file:
        file.write(response.content)