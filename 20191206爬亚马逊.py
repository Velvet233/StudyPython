import requests
from bs4 import BeautifulSoup

#crawl the html

URL="https://www.amazon.cn/gp/product/B01FJ6MZG6?pf_rd_p=c6d17c3b-92ef-4aa7-920b-19155bc9b830&pf_rd_s=merchandised-search-7&pf_rd_t=101&pf_rd_i=1403206071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=9R8J8C9VB7GA37004GPG&ref=cn_ags_floor_hotasin_1403206071_mobile-1"

#Use chrome chrome://version/ to check your user-agent
#you can also use IETF's tools(https://tools.ietf.org/html/) page to choose headers

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Accept': 'text/*;q=0.3, text/html;q=0.7, text/html;level=1,text/html;level=2;q=0.4, */*;q=0.5',
    'Accept-Charset': 'iso-8859-5, unicode-1-1;q=0.8',
    'Accept-Encoding': 'gzip;q=1.0, identity; q=0.5, *;q=0',
    'Accept-Language': 'da, en-gb;q=0.8, en;q=0.7',
    'DNT':'1',#dont track request header
    'Connection':'close'
}

#Internet Engineering Task Force(IETF)构成了tcp，http的一个标准
#IETF Tools里面的标准 网页https://tools.ietf.org/
#https://tools.ietf.org/html/

page=requests.get(URL,headers=headers)

soup_obj=BeautifulSoup(page.centent,"html.parser")

product_name=soup_obj.find(id='productTitle').get_text()
product_price=soup_obj.find(id='product_ourprice').get_text()
convert_product_prive_string_to_float=float(product_price[1:7].replace(",",""))

print(product_name.strip())
print(product_price.strip())


#print(soup_obj.prettify())


