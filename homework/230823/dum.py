import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox
import re

#
ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

# 가져올 항목
posterImgUrl, title, rating = "", "", ""


# 특수문자 삭제

def clean_text(inputString):
    text_rmv = re.sub(
        '[-=+,#/\?:^@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
    return text_rmv


# insert 함수
def insertData(title, rating, posterImgUrl):
    # con : 파이썬 <-> mysql 연결하기 위한 인스턴스, 도구
    # cur : 디비의 정보를 조작하기 위한 도구
    con, cur = None, None
    data1, data2, data3 = "", "", ""
    # sql 연결
    con = pymysql.connect(host='127.0.0.1', user='root',
                          password='1234', database='crawlingtestdb', charset='utf8')
    # cursor : 하나의 DB connection에 대하여
    # 독립적으로 SQL 문을 실행할 수 있는 작업환경을 제공하는 객체.
    cur = con.cursor()

# CREATE TABLE `crawlingtestdb`.`GoldenerBearTable` (
#   `num` INT AUTO_INCREMENT,
#   `title` VARCHAR(200) NULL,
#   `rating` VARCHAR(100) NULL,
#   `posterImgUrl` VARCHAR(400) NULL,
#   PRIMARY KEY (`num`));

    data1 = title
    data2 = rating
    data3 = posterImgUrl

    try:
        query = "INSERT INTO GoldenerBearTable (title, rating, posterImgUrl) VALUES (%s, %s, %s)"
        values = (data1, data2, data3)
        cur.execute(query, values)
    except:
        print("데이터 입력 오류가 발생")
    else:
        print("데이터 입력 성공!")
    con.commit()
    con.close()


#
count = 1
watchaUrl = "https://pedia.watcha.com/ko-KR/staffmades/611"
while True:
    if (count != 10):
        try:
            htmlObject = urllib.request.urlopen(watchaUrl, context=ssl_context)
            webPage = htmlObject.read()
            bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
            tag_list = bsObject.findAll(
                'li', {'class': 'e1w9y4r09'})
            # tag_list = bsObject.findAll(
            #     'li', {'class': 'css-1ofozqs e1w9y4r09'})
            # print(f"tag_list 갯수 : {len(tag_list)} ")
            # print(f"tag_list 결과 : {tag_list} ")
            print("===베를린영화제 황금곰상 수상작===")
            for tag in tag_list:
                if (count != 10):
                  #   제목
                    title = tag.find('div', {'class': 'e1w9y4r05'}).text
                    title = clean_text(title)
                    print(f"title:{title}")
                  #   별점
                    rating = tag.find('div', {'class': 'e1w9y4r04'}).text
                    rating = clean_text(rating)[-3:]
                    print(f"rating:{rating}")
                  #   이미지
                    posterImgUrl = tag.find(
                        'img', {'class': 'ezcopuc0'})['src']
                    print(f"posterImgUrl : {posterImgUrl}")
                  #   DB에 넣기
                    insertData(title, rating, posterImgUrl)
                  #   카운트 추가
                    count += 1
        except:
            break
