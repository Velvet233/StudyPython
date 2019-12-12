import requests
import json

def get_and_download_pdf():
    #we need to add referer to show that we are inside the web
    response=requests.get('http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?jsonCallBack=jsonpCallback97604&isPagination=true&productId=&keyWord=&securityType=0101&reportType2=&reportType=ALL&beginDate=2019-01-01&endDate=2019-01-30&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1576040173383p.endPage=5&_=1576038378952',
    headers={'Referer':'http://www.sse.com.cn/disclosure/listedinfo/announcement/'})

    string_to_be_loaded=response.text[19:-1]

    formatted_data=json.loads(string_to_be_loaded)#一系列的数据
    for every_report in formatted_data['result']:
        pdf_url="http://static.sse.com.cn/"+every_report['URL']
        print(pdf_url)
        file_name=every_report['TITLE']+'.pdf'
        resource = requests.get(pdf_url,stream=True)#下载
        with open(file_name,'wb') as temp:
            for chunk in resource.iter_content(1024):
                temp.write(chunk)
            print("上市公司报告:"+file_name+",已经完成下载")

#外部调用程序
if __name__=="__main__" :
    get_and_download_pdf()
