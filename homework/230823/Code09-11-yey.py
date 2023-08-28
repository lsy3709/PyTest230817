import bs4
import urllib.request

import ssl
import pymysql
from tkinter import *
from tkinter import messagebox
import re
import time

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
week, te, imgsrc = "", "", ""
null = None

def clean_text(inputString):
    text_rmv = re.sub(
        '[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
    return text_rmv

# 10.10.10.10 : 집 DB 서버 주소
def insertData(week, te, imgsrc):
    con, cur = None, None
    data = ""
    data0, data1, data2, data3 = "", "", "", ""
    sql = ""
    con = pymysql.connect(host='10.10.10.10', user='root',
                          password='1234', database='site', charset='utf8')
    cur = con.cursor()

    data1 = week
    data2 = te
    data3 = imgsrc

    # data1 = clean_text(subject)
    # data2 = clean_text(press)
    # data3 = clean_text(pDate)
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
        query = "INSERT INTO wether (week, te, imgsrc) VALUES (%s, %s, %s)"
        # 문법 틀린 부분 ? -> %s 변경시 됨.
        values = (data1, data2, data3)
        # sql = "INSERT INTO newsTable (title,publisher,newsDate,newsTime,newsDetail,newsImgUrl)  VALUES('" + \
        #     data1 + "','" + data2 + "','" + data3 + "','" + \
        #     data4 + "','" + data5 + "','"+data6 + "')"
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


nateUrl = "https://news.nate.com/weather"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div -> 속성 : class, 값 : snbArea
tag = bsObject.find('div', {'class':'oneweek_wrap'})

print('## 네이트 뉴스의 메뉴 목록 ##')
# div -> 속성 값 : class, 값 : snbArea의 값을 리스트에 저장
li_list = tag.findAll('li')
print(f"li_List 의 값 목록 : {li_list}")
for lis in li_list :
    print("------------------------------------------------")
    print(lis.text, end='  ' )
    a_tag = lis.find("p",{"class":"day"})
    print(f"li 태그의 값 : {a_tag}")
    print("********************************************")
    print(f"li 태그의 값 : {a_tag.text}")
    print("------------------------------------------------")
    a_te = lis.find("p", {"class" : "te"})
    print(f"li 태그의 값 : {a_te.text}")
    print("------------------------------------------------")
    imgurl = lis.find("img")
    imgurl_src = imgurl['src']
    print(f"li 태그의 값 : {imgurl_src}")
    
    insertData(a_tag.text, a_te.text, imgurl_src)

'''콘솔에 찍는거는 성공 !!!!!'''