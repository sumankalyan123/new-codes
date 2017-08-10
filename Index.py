from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import urllib.request
import lxml.html
import os
import random


def read_from_text_file(filename):
    songs = []
    names_with_download_tag = []
    for line in open(filename, 'r').readlines():
        songs.append(line.strip())
        names_with_download_tag = [x + ' download mp3 song jatt ' for x in songs]
        return names_with_download_tag


def search_google(songname):
    url = 'https://www.google.co.in/search?q=' + songname
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"lxml")
    import re
    google_search_url_list = []
    links = soup.findAll("a",'href')
    for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        href = str(re.split(":(?=http)",link["href"].replace("/url?q=","")))
        href_replaced = href[:href.find('.html')+5]
        if 'webcache' not in href_replaced:
            if 'http' in href_replaced:
                google_search_url_list.append(href_replaced)
    return google_search_url_list

def get_all_download_links(song_link_from_google):
    download_links = []
    for url in song_link_from_google:
        source_code = requests.get(url, allow_redirects=False)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all("a"):
            href = str(link.get('href'))
            if href.endswith('.mp3'):
                download_links.append(href)
        return download_links



def download_web_image(url):
    for song in url:
        name = random.randrange(1, 1000000)
        full_name = str(name) + ".mp3"
        urllib.request.urlretrieve(song, full_name)


#name = read_from_text_file('names.txt')
#google_links_list = google_search(name)
#print(google_links_list)
write_all_download_links('https://mp3mad.com/download-1770/Jadu-Teri-Nazar-Udit-Narayan.html')
song_download_link = read_from_temp_file()
print (song_download_link)
download_web_image(song_download_link)

