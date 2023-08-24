import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox
import re


# 주의사항, 문자열 안에 특수문자 부분 체크 잘하기

# 현재 네이트 기사는 특정 시간 예 1분마다 새로운 기사가 나옴

# 그래서 현재 페이지에 1페이지에서 20개 기사만 디비에 저장하기로 함

# 특정 시간 time.sleep(300), 5분정도 인터벌을 두고 저장하기로 함

# 예스24는 한페이지의 상품이 고정
# 뉴스는 실시간으로 계속 생성됨

# 아래코드, 웹 상에 접근 시 인증된 여부를 확인시 필요한 부분
# ssl 설정을 none 했음
# 맥북 테스트, 아래 오류가 발생해서 임시 방편으로 처리한 코드
ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
imgLinkUrl, title, rate, star = "", "", "", ""
# null = None


# 함수 선언 부분
# regex 이용해서 re.sub (매개변수1, 매개변수2, 매개변수3)
# 매개변수1 : 특정 조건
# 매개변수2 : 대체할 문자
# 매개변수3 : regex를 적용할 문장
def clean_text(inputString):
    text_rmv = re.sub(
        '[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
    return text_rmv

# 가져올 정보를 pymysql를 이용해서 실제로 추가하는 부분
def insertData(imgLinkUrl, title, price, startYN):
    # con : 파이썬 <-> mysql 연결하기위한 인스턴스 도구
    # cur : 디비의 정보를 조작하기위한 도구
    con, cur = None, None
    data = ""
    data0, data1, data2, data3 = "", "", "", ""
    sql = ""
    con = pymysql.connect(host='127.0.0.1', user='root',
                          password='1234', database='MovieTest', charset='utf8')
    cur = con.cursor()

#   `imgLinkUrl` VARCHAR(200) NULL,
#   `title` VARCHAR(45) NULL,
#   `price` VARCHAR(10) NULL,

    # data0 = data10
    data1 = imgLinkUrl
    data2 = title
    data3 = price

    if startYN == True:
        cur.execute("TRUNCATE TABLE MovieTable")
 
    #
    try:
        query = "INSERT INTO MovieTable (imgLinkUrl, title, price) VALUES (%s, %s, %s)"
        # 문법 틀린 부분 ? -> %s 변경시 됨
        values = (data1, data2, data3)
        print("순서2 : sql 실행전 ")
        print(f"sql : {sql}")

        # cur.execute(sql)

        cur.execute(query, values)
        
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



##
page = 1
count = 1
MovieUrl = "https://www.yes24.com/24/Category/BestSeller?CategoryNumber=003&sumgb=06"
startYN = True
while True:
    if (count != 21):
        try:
            # newsUrl = nateUrl + str(page)
            MovieUrl = MovieUrl
            # page += 1
            htmlObject = urllib.request.urlopen(MovieUrl, context=ssl_context)
            webPage = htmlObject.read()
            bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
            tag_list = bsObject.find('ol', {'class': 'grid'})
            #print(f"tag_list 개수 : {len(tag_list)} ")
            #print(f"tag_list 내용 : {tag_list} ")
            print('###### 실시간 Yes24 속보 #######')
            lilist = tag_list.findAll('li')
            #print(lilist)
            #print("==========")
            for tag in lilist:
                #print(count, tag)
                #print("==========")
                if (count != 21):
                    title = tag.find('p', {'class' : 'title'}).text
                    price = tag.find('p', {'class' : 'price'}).text
                    imgLinkUrl = tag.find('img')['src']
                
                        # continue
                    print("순서1: 데이터 추가 전")
                    print("imgLinkUrl: %s" % (imgLinkUrl))
                    print("title: %s" % (title))
                    print("price: %s" % (price))
                    print('================================')
                    print('================================')
                    insertData(imgLinkUrl, title, price, startYN)
                    startYN = False
                    count += 1
                   
        except:
            break
    else:
         break
        # time.sleep(10)
        # startYN = True
        # count = 1