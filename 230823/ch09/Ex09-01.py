import time
import bs4
import urllib.request

nateUrl = "https://news.nate.com/recent?mid=n0100"
while True :
    htmlObject = urllib.request.urlopen(nateUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.findAll('div', {'class': 'mlt01'})

    print('###### 실시간 뉴스 속보 #######')
    num = 1
    for tag in tag_list :

        subject = tag.find('strong', {'class': 'tit'}).text
        link = tag.find('a', {'class': 'lt1'})['href']
        pressAndDate = tag.find('span', {'class': 'medium'}).text
        pressAndDate.replace('\t',' ')
        pressAndDate.replace('\n', '')

        if len(pressAndDate.split()) == 3 :
            press, pDate, pTime = pressAndDate.split()
        elif len(pressAndDate.split()) == 4 :
            press1,press2, pDate, pTime = pressAndDate.split()
            press = press1+press2
        else :
            continue

        print('(' , num, ')', subject)
        print('\t https:'+link, press, pDate, pTime)
        num += 1

    time.sleep(60)