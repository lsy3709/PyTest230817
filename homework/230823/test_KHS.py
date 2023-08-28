import bs4
import urllib.request
import ssl
import pymysql
import re
import time

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE


def clean_text(inputString):
    text_rmv = re.sub(
        '[-=+,#/\?:^.@*\"※~ㆍ!』‘\(\)\[\]`\'…》\”\“\’·]▶ ', ' ', inputString)
    return text_rmv


def insertData(title, desc, price, link, imgLinkUrl):
    try:
        con = pymysql.connect(host='127.0.0.1', user='root',
                              password='1234', database='Linken', charset='utf8')
        cur = con.cursor()

        sql = "INSERT INTO Linken (title, desc1, price, link, ImgUrl) VALUES (%s, %s, %s, %s, %s)"
        print(f"title : 결과 : {title}")
        print(f"desc : 결과 : {desc}")
        print(f"price : 결과 : {price}")
        print(f"link : 결과 : {link}")
        print(f"ImgUrl : 결과 : {imgLinkUrl}")
        print(f"sql : 결과 : {sql}")
        data = (title, desc, price, link, imgLinkUrl)
        cur.execute(sql, data)

        con.commit()

    except Exception as e:
        print('================================')
        print("순서3 : 예외 발생")
        print(e)
        print('================================')
    finally:
        if con:
            con.close()


LinkenUrl = "http://linkandleave.com/?r=home&c=region/61/81"
try:
    count = 1
    while count <= 20:
        LinkenleaveUrl = LinkenUrl
        htmlObject = urllib.request.urlopen(
            LinkenleaveUrl, context=ssl_context)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag_list = bsObject.findAll('div', {'class': 'thumbnail'})

        print('###### 유럽 여행 가이드 #######')
        for tag in tag_list:
            if count > 20:
                break

            title = clean_text(
                tag.find('div', {'class': 'title ellipsis-multi st-font1'}).text.strip())
            link = 'http://linkandleave.com' + tag.find('a')['href']
            imgLink = tag.find('div', {'class': 'image'})
            imgLinkUrl = '이미지가 존재하지 않음'
            if imgLink and imgLink.has_attr('style'):
                imgLinkUrl = re.search(
                    r"url\('(.*)'\)", imgLink['style']).group(1)
            # Find the desc element
            desc_elem = tag.find('div', {'class': 'desc ellipsis'})
            desc = '설명이 없습니다'  # Default value in case desc element is not found
            if desc_elem:  # Check if desc element is found
                # Update desc with actual value
                desc = clean_text(desc_elem.text.strip())

            price = clean_text(tag.find('div', {'class': 'price'}).find(
                'h6', {'class': 'won'}).text.strip())

            print("순서1: 데이터 추가 전")
            print("title:", title)
            print("desc:", desc)
            print("price:", price)
            print("link:", link)
            print("imgLinkUrl:", imgLinkUrl)
            print("count:", count)
            print('================================')
            print('================================')
            insertData(title, desc, price, link, imgLinkUrl)
            count += 1
        time.sleep(60)

except Exception as e:
    print(e)
