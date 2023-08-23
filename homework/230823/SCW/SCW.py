import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox
import re

# 주의사항, 문자열 안에 특수문자 부분 체크 잘하기.
# 현재 네이트 기사는 특정 시간 예 1분마다 새로운 기사가 나옴.
# 그래서, 현재 페이지에 1페이지에서 20개 기사만 디비에 저장하기로 함.
# 특정 시간 time.sleep(300), 5분정도 인터벌을 두고 저장하기로 함.
# 예스24는 한페이지의 상품이 고정,
# 뉴스는 실시간으로 계속 생성됨.
ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
img, title, auth, publisher, date, price = "", "", "", "", "", ""
null = None
# 함수 선언 부분


def clean_text(inputString):
    text_rmv = re.sub("[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`'…》\”\“\’·]", " ", inputString)
    return text_rmv


def insertData(img, title, auth, publisher, date, price):
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5, data6 = "", "", "", "", "", "", ""
    sql = ""
    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="yes24itdb",
        charset="utf8",
    )
    cur = con.cursor()
    #    title` VARCHAR(200) NULL,
    #   `publisher` VARCHAR(45) NULL,
    #   `newsDate` VARCHAR(10) NULL,
    #   `newsTime` VARCHAR(6) NULL,
    #   `newsDetail` VARCHAR(200) NULL,
    #   `newsImgUrl` VARCHAR(200) NULL,
    # data0 = data10
    data1 = img
    data2 = title
    data3 = auth
    data4 = publisher
    data5 = date
    data6 = price
    # data1 = clean_text(subject)
    # data2 = clean_text(press)
    # data3 = clean_text(pDate)
    # data4 = clean_text(pTime)
    # data5 = clean_text(link)
    # data6 = clean_text(imgLinkUrl)
    #
    try:
        # print(null)
        # print("데이터 실행전 확인")
        # print(data1)
        # print(data2)
        # print(data3)
        # print(data4)
        # print(data5)
        # print(data6)
        # query = "INSERT INTO newsTable (title, publisher, newsDate, newsTime, newsDetail, newsImgUrl) VALUES (?, ?, ?, ?, ?, ?)"
        # values = (data1, data2, data3, data4, data5, data6)
        sql = (
            "INSERT INTO itproduct (imgLinkUrl, title, auth, pub, date, price)  VALUES('"
            + data1
            + "','"
            + data2
            + "','"
            + data3
            + "','"
            + data4
            + "','"
            + data5
            + "','"
            + data6
            + "')"
        )
        # print("순서2 : sql 실행전 ")
        # print(f"sql : {sql}")

        cur.execute(sql)

        # cur.execute(query, values)
    except:
        print("================================")
        print("순서3 : 예외 발생")
        print("================================")
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else:
        print("================================")
        print("순서3: 성공")
        print("================================")
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()


##
page = 1
count = 0
offset = 0
yes24Url = "https://www.yes24.com/24/Category/Display/001001003022?PageNumber=" + (str)(
    page
)
print("yes24 신규 IT 책 목록")
while True:
    if count != 21:
        try:
            htmlObject = urllib.request.urlopen(yes24Url, context=ssl_context)
            webPage = htmlObject.read()
            bsObject = bs4.BeautifulSoup(webPage, "html.parser")
            tag_list = bsObject.findAll("div", {"class": "cCont_goodsSet"})
            for tag in tag_list:
                if count != 21:
                    # strong -> h2 변경 230629 (확인 날짜)
                    # img, titleUrl, auth, publisher, date, price
                    title = tag.find("div", {"class": "goods_name"}).text
                    price = tag.find("em", {"class": "yes_b"}).text
                    imgLink = tag.find("span", {"class": "imgBdr"}, "a")
                    # 이미지 없는 경우 처리 부분. 파이썬 null 대신  None
                    if imgLink != None:
                        imgLinkUrl = imgLink.find("img")["src"]
                        imgLinkUrl = "https:" + imgLinkUrl
                    else:
                        imgLinkUrl = "이미지가 존재 하지 않음"

                    auth = tag.find("div", {"class": "goods_pubGrp"}, "span").text

                    publisher = tag.find("span", {"class": "goods_pub"}).text

                    date = tag.find("span", {"class": "goods_date"}).text

                    print("순서1: 데이터 추가 전")
                    print("title: %s" % (title))
                    print("auth: %s" % (auth))
                    print("publisher: %s" % (publisher))
                    print("date: %s" % (date))
                    print("price: %s" % (price))
                    print("count : %d" % count)
                    print("================================")
                    print("================================")
                    insertData(imgLinkUrl, title, auth, publisher, date, price)
                    count += 1
                    page += 1
        except:
            break
    else:
        break
        # time.sleep(60)
