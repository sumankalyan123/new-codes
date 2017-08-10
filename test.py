import requests
from bs4 import BeautifulSoup

def search(urls):
    list = []
    url = urls[0]
    source_code = requests.get(url, allow_redirects=False)
    plain_text = source_code.text.encode('ascii', 'replace')
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.find_all("a"):
                href = str(link.get('href'))
                if href.endswith('.mp3'):
                    list.append(href)
    return  list

url = ['https://mr-jatt.com/album/hindi-single-songs/arijit-singh-mere-rashke-qamar-rbxc.html']
name = search(url)
print(name)

