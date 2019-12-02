from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
#多层网页跳转抓取

link=['https://guba.eastmoney.com/']
def get_all_link(url):
    html=urlopen(url)
    bso=BeautifulSoup(html,"parser")
    for link in bso.findAll("a"):
        if "href" in link.attrs:
            #print("This is newly appended URL "+link.attrs["href"])
            link.append(link.attrs["href"])
            
get_all_link("http://guba.eastmoney.com/")
print(links)
