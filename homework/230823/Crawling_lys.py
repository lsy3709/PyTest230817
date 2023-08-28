import bs4
import urllib.request
import pymysql
from tkinter import *



#전역변수
title, author, publisher, price, imgUrl = "","","","",""


def insertData(title,author,publisher,price,imgUrl):
    con, cur = None, None
    
    data1, data2, data3, data4, data5 ="","","","",""

    con=pymysql.connect(host='127.0.0.1', user='root',
                        password='1234', database='aladinBooksLive', charset='utf8')
    cur=con.cursor()

    data1=title
    data2=author
    data3=publisher
    data4=price
    data5=imgUrl

    try:
        query = "INSERT INTO booksTable (title,author,publisher,price,imgUrl) VALUES (%s, %s, %s, %s, %s)"
        values = (data1, data2, data3, data4, data5)
        cur.execute(query, values)
    except Exception as e:
        print("================================")
        print("순서3 : 예외 발생 : ",e)
        print("================================")
    else:
        print("================================")
        print("순서3 : 성공")
        print("================================")
    con.commit()
    con.close()



page = 1
while True:
      try:
          
          booksUrl = f"https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page={page}&Stockstatus=1&PublishDay=84&CID=437&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="
          count =1

          # booksUrl = aladinUrl
          htmlObject = urllib.request.urlopen(booksUrl)
          webPage = htmlObject.read()
          bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
          tag_list = bsObject.findAll('div', {'class': 'ss_book_box'})

          for tag in tag_list:
              if(count!=26):
                  #이미지
                  imgPlate = tag.find('div',{'class':'flipcover_in'})
                  imgUrl = imgPlate.find_all('img')[-1]['src']

                  #제목
                  title = tag.find('a',{'class':'bo3'}).text
                  
                  listPlate = tag.find('div',{'class':'ss_book_list'})
                  listUl = listPlate.find('ul')
                  listLi = listUl.find_all('li')[2]
                  #저자
                  author = listLi.find_all('a')[0].text
                  #출판사
                  publisher = listLi.find_all('a')[1].text
                  
                  #가격
                  pricePlate = tag.find('span',{'class':'ss_p2'})
                  priceUl = pricePlate.find('b')
                  price = priceUl.find('span').text


                  print("=====순서1: 데이터 추가 전=====")
                  print(title)
                  print(author)
                  print(publisher)
                  print(price)
                  print(imgUrl)
                  print("================================")
                  insertData(title, author, publisher, price, imgUrl)
                  count += 1
          
          
      except Exception as e:
          print("Error:", e)

      count=1
      page += 1

