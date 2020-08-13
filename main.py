from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "E:\covoid_notify\iconico.ico",
        timeout = 15
    )
def getData(url):
    r=requests.get(url)
    return r.text
if __name__ == "__main__":
    while True:    
        myHtmlData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
            myDataStr = myDataStr[1:]
            itemList = myDataStr.split("\n\n")
        states = ['Maharashtra','Telengana','Utter Pradesh']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                nTitle = "cases of covoid-19"
                nText = f"state {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured : {dataList[4]}\nDeaths : {dataList[5]}"
                notifyme(nTitle , nText)
                time.sleep(2)
        time.sleep(3600)









        


