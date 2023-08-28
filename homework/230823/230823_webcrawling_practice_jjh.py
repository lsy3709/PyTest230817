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
movietitle, watchlevel, moviedetail, whenstart, howmanypeople, posterimgUrl = "", "", "", "", "", ""
null = None

def clean_text(inputStr):
    txt_rmv = re.sub(
         '[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]', ' ', inputStr)
    return txt_rmv

def insertMovie(movietitle, watchlevel, moviedetail, whenstart, howmanypeople, posterimgUrl, firstYN):
    print(posterimgUrl)
    con, cur = None, None
    data1 = movietitle
    data2 = watchlevel
    data3 = moviedetail
    data4 = whenstart
    data5 = howmanypeople
    data6 = posterimgUrl

    con = pymysql.connect(host='127.0.0.1', user='root', password='1433', database='movieDB', charset='utf8')
    cur = con.cursor()

    if firstYN == True:
        cur.execute("TRUNCATE TABLE movieChart")

    try:
        query = "INSERT INTO movieChart (movietitle, watchlevel, moviedetail, whenstart, howmanypeople, imgLinkUrl) Values (%s, %s, %s, %s, %s, %s)"
        values = (data1, data2, data3, data4, data5, data6)
        print("sql 실행 전")
        cur.execute(query, values)
        print("sql 실행 완료")    
    except:
        print('================================')
        print("예외 발생")
        print('================================')
    else:
        print('================================')
        print("데이터 입력 완료")
        print('================================')
    con.commit()
    con.close()


page = 1
count = 1
movieUrl =  "https://movie.daum.net/ranking/boxoffice/weekly"
firstYN = True
finishFlag = True
while True:
    if finishFlag == True:
        try:
            htmlObj = urllib.request.urlopen(movieUrl, context=ssl_context)
            print("try2")
            webPage = htmlObj.read()
            bsObj   = bs4.BeautifulSoup(webPage, 'html.parser')
            tag_list = bsObj.findAll('div', {'class' : 'item_poster'})
            for tag in tag_list:
                # print(f"tag :: {tag}")
                movietitle   = tag.find('a', {'class' : 'link_txt'}).text
                posterimgUrl = tag.find('img', {'class' : 'img_thumb'})
                watchlevel   = tag.find('span', {'class' : 'ico_movie'}).text
                moviedetail  = tag.find('a', {'class' : 'link_story'}).text.strip()
                movieinfo    = tag.findAll('span', {'class' : 'info_txt'})
                whenstart    = (movieinfo[0].text)[2:]
                howmanypeople= (movieinfo[1].text)[3:]
                # print(movietitle.text)
                print(posterimgUrl['src'])
                # print(watchlevel.text)
                # print(moviedetail.text.strip())
                # print(whenstart)
                # print(howmanypeople)
                # break
                if posterimgUrl == None:
                    posterimgUrl = "이미지가 없음"
                if howmanypeople == None:
                    howmanypeople = "집계된 관객수가 없음"
                insertMovie(movietitle, watchlevel, moviedetail, whenstart, howmanypeople, posterimgUrl['src'], firstYN)
                firstYN = False
            finishFlag = False
        except:
            print("exception")
            break
    else:
        break
