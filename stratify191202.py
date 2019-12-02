#层级介绍
from urllib.request import urlopen
#from urllib.error import HTTPError
#from urllib.error import URLError
from bs4 import BeautifulSoup

html=urlopen("http://www.eastmoney.com/")
bso=BeautifulSoup(html."html.parser")

for descendant in bso.find("div",{"class":"nlist"}).descendants:
    print(descendant)
