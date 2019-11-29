from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.wikipedia.org/')
#用html.parser来进行解析
bso=BeautifulSoup(html,"html.parser")

a_list=bso.findall("div",{class=''})

for item in a_list:
    print(item.get_text())
