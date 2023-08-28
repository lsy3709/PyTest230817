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
artist, songtitle, albumtitle, thumbnailurl = "", "", "", ""
null = None

def clean_text(inputStr):
    txt_rmv = re.sub(
         '[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]', ' ', inputStr)
    return txt_rmv

def insertMusic(artist, songtitle, albumtitle, thumbnailurl, firstYN):
    con, cur = None, None
    data1 = artist
    data2 = songtitle
    data3 = albumtitle
    data4 = thumbnailurl

    con = pymysql.connect(host='127.0.0.1', user='root', password='1433', database='bugsDB', charset='utf8')
    cur = con.cursor()

    if firstYN == True:
        cur.execute("TRUNCATE TABLE musicChart")

    try:
        query = "INSERT INTO musicChart (artist, songtitle, albumtitle, thumbnailurl) Values (%s, %s, %s, %s)"
        values = (data1, data2, data3, data4)
        #print("sql 실행 전")
        cur.execute(query, values)
        #print("sql 실행 완료")    
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
coinUrl =  "https://music.bugs.co.kr/chart"
firstYN = True
finishFlag = True
while True:
    if finishFlag == True:
        try:
            print(coinUrl)
            htmlObj = urllib.request.urlopen(coinUrl, context=ssl_context)
            print("try2")
            webPage = htmlObj.read()
            bsObj   = bs4.BeautifulSoup(webPage, 'html.parser')
            tag_list = bsObj.findAll('tr')
            for tag in tag_list:
                #print(f"tag :: {tag}")
                thumbnailurl = tag.find('img')
                songtitle    = tag.find('p', {'class' : 'title'})
                artist       = tag.find('p', {'class' : 'artist'})
                albumtitle   = tag.find('a', {'class' : 'album'})
                if thumbnailurl == None:
                    thumbnailurl = "썸네일 없음"
                else:
                    thumbnailurl = thumbnailurl['src']
                if songtitle == None:
                    songtitle = "곡제목 없음"
                else:
                    songtitle = songtitle.text
                if artist == None:
                    artist = "가수 없음"
                else:
                    artist = artist.text
                if albumtitle == None:
                    albumtitle = "앨범 없음"
                else:
                    albumtitle = albumtitle.text
                insertMusic(artist, songtitle, albumtitle, thumbnailurl, firstYN)
                firstYN = False
            finishFlag = False
        except:
            print("exception")
            break
    else:
        time.sleep(30)
        finishFlag = True
        firstYN = True
