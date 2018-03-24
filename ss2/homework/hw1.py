from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
html_content = conn.read().decode('utf8')

soup = BeautifulSoup(html_content, "html.parser")

section = soup.find("section", "section chart-grid")
li_list = section.find_all('li')
datas = []
for li in li_list:
    data = {}
    data['title'] = li.h3.a.string
    data['artist'] = li.h4.a.string
    datas.append(data)
pyexcel.save_as(records=datas, dest_file_name="itunes.xls")
for li in li_list:
    options = {
    'default_search' : 'ytsearch',
    'max_download' : 1,
    }
    dl = YoutubeDL(options)
    song = li.h3.a.string
    artist = li.h4.a.string
    dl.download([song and artist])
