from urllib.request import urlopen
url = "http://dantri.com.vn/"
#1. Download web page
#1.1 Open conncetion
conn = urlopen(url)
#1.2Read
html_content = conn.read().decode('utf8')
#1.3 Decode
# html_content = data.decode("utf8")
# save html_content to file
# html_file = open("dantri.html", "wb")
# html_file.write(html_content)
# html_file.close()


#2 Track region of interest:
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser") #html, xml, xhtml

ul = soup.find("ul", "ul1 ulnew") #only for addClass
# print(ul.prettify())

#3. Extract info:
li_list = ul.find_all("li")
# for li in li_list:
#     print(li.prettify())
#     print('*' *30)
# for li in li_list:
#
#     a = li.h4.a
#     print(url + a['href'])
#     print(a.string)

import pyexcel
datas = []
for li in li_list:
    data ={}
    a = li.h4.a
    data["title"] = a.string
    data["link"] = url + a["href"]
    datas.append(data)
pyexcel.save_as(records=datas, dest_file_name="dan.xls")
