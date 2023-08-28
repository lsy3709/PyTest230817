import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox
import re

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
name, auth, price, publisher, goodsImgUrl= "","", "", "", ""

def clean_text(inputString):
    text_rmv = re.sub(
        '[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
    return text_rmv

def insertData(name,auth, price, publisher, goodsImgUrl):
    # con : 파이썬 <-> mysql 연결하기 위한 인스턴스, 도구
    # cur : 디비의 정보를 조작하기 위한 도구
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5= "", "", "", "", "",""
    sql = ""
    con = pymysql.connect(host='127.0.0.1', user='root',
                          password='1234', database='yes24goods', charset='utf8')
    cur = con.cursor()
#    title` VARCHAR(200) NULL,

#   `num` INT AUTO_INCREMENT,
#   `name` VARCHAR(200) NULL,
#   `price` VARCHAR(6) NULL,
#   `auth` VARCHAR(200) NULL,
#   `goodsImgUrl` VARCHAR(200) NULL
    # data0 = data10
    data1 = name
    data2 = auth
    data3 = price
    data4 = publisher
    data5 = goodsImgUrl
  
    #
    try:
        # print(null)
        # print("데이터 실행전 확인")
        # print(data1)
        # print(data2)
        # print(data3)
        # print(data4)
        # print(data5)
        query = "INSERT INTO goodsTable (name, auth, price, publisher,goodsImgUrl ) VALUES (%s, %s, %s, %s, %s)"
        values = (data1, data2, data3, data4, data5)
        print("순서2 : sql 실행전 ")
        cur.execute(query,values)
    except:
        print('================================')
        print("순서3 : 예외 발생")
        print('================================')
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else:
        print('================================')
        print("순서3: 성공")
        print('================================')
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()

#
#  data1 = name
    # data2 = price
    # data3 = goodsDetail
    # data4 = goodsImgUrl
    #name,auth, price, publisher, goodsImgUrl
page = 1
count = 1
yes24Url = "https://www.yes24.com/24/Category/Display/006001099"
while True:
    if (count != 21):
        try:
            # newsUrl = nateUrl + str(page)
            goodsUrl = yes24Url
            # page += 1
            htmlObject = urllib.request.urlopen(goodsUrl, context=ssl_context)
            webPage = htmlObject.read()
            bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
            tag_list = bsObject.find('ul', {'class': 'clearfix'})
            # print(f"tag_list: {tag_list}")
            # print(f"tag_list: {len(tag_list)}")
            print('###### 굿즈현황 ###### #')
            li_all_list = bsObject.findAll('li')
            for tag in li_all_list:
                if (count != 21):
                    # strong -> h2 변경 230629 (확인 날짜)
                    name = tag.find('img')['alt']
                    name = clean_text(name)
                    # print(f"{name}")
                    # link = tag.find('a', {'class': 'lt1'})['href']
                    # link = 'https:' + link
                    goodsImgUrl = tag.find('img')['src']
                    # 이미지 없는 경우 존재하지 않음
                    if goodsImgUrl == None:
                       goodsImgUrl = '이미지가 존재 하지 않음'
                    
                    
                    
                    print(goodsImgUrl)
                    auth = tag.find('span', {'class': 'goods_auth'}).text
                    publisher = tag.find('span', {'class': 'goods_pub'}).text
                    price = tag.find('em', {'class': 'yes_b'}).text
                        # continue
                    print("순서1: 데이터 추가 전")
                    print("name: %s" % (name))
                    print("auth: %s" % (auth))
                    print("price: %s" % (price))
                    print("publisher: %s" % (publisher))
                    print("goodsImgUrl: %s" % (goodsImgUrl))
                    print('================================')
                    print('================================')
                    insertData(name, auth, price, publisher, goodsImgUrl)
                    count += 1
                    # print('(' , page, ')', subject)
                    # print('\t https:'+link, press, pDate, pTime)
                    # print('\t imgLink : '+ imgLinkUrl)
                    # auth, price, publisher,goodsImgUrl
                    print(count)
        except:
            break
    else:
        break
    # time.sleep(60)
