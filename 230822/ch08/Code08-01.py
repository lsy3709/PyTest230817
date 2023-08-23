# SQLite 데이터베이스에 스키마 생성, 테이블 생성해서.
# 파이썬 버전으로 접근해서, 데이터 게터/세터
# 크롤링 한 데이터를 , 임시 메모리 저장 -> 해당 디비 쓰기작업
# 특정 시간 마다, 입력이 되게끔 설정.
# 1) cmd -> 스키마 생성 및 테이블 생성, crud
# sqlite 설치한 폴더 : c 드라이브 밑으로 이동 했나요?
# 확인용 -> 이런것도 있다라는 소개.

# 했으면 해당 폴더에 가서 샘플로 만들어 볼게요.

# 2) DB Browser for SQLite(워크벤치) : GUI 로 간단히
#  스키마 생성 및 crud

# sqlite 접근하기위한 모듈 도구 모음
import sqlite3

# 해당 데이터베이스 연결 하기위한 인스턴스
con = sqlite3.connect("naverDB")
# 해당 데이터베이스에서 cursor (특정 테이블에 접근하기 위한 도구. )
cur = con.cursor()

# 터미널에서 입력 받은 데이터를 , 테이블에 저장 하는 예제.
while (True):
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + \
        "','" + data2 + "','" + data3 + "', " + data4 + ")"
    # sql 문장을 cur (커서로) C(insert)
    cur.execute(sql)
# 저장.
con.commit()
con.close()
