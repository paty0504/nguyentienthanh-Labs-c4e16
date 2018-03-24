from bs4 import BeautifulSoup
import pyexcel
from urllib.request import urlopen
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/1/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
html_content = conn.read().decode('utf8')
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find('table', id='tableContent')
trlist = table.fill_all('tr')
datas = []

fields = ['noi_dung','quy 4_2016','quy 1_2017','quy 2_2017','quy 3_2017']
for tr in tr_list:
    td_list = tr.find_all("td")
    td_list = td_list[:-1]
    if len(td_list) == 0:
        continue
    data={}
    for i in range(len(fields)):
        data[fields[i]] = td_list[i].string
    datas.append(data)

pyexcel.save_as(records=datas,dest_file_name="caffe.xls")
