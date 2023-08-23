import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

## 메인 코드 부분 ##
con = sqlite3.connect("testDB230822.db")
cur = con.cursor()

cur.execute("SELECT * FROM userTest")

print("사용자ID       이메일            패스워드")
print("--------------------------------------------------------")

while (True):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    print("%5d   %30s   %30s  " % (data1, data2, data3))

con.close()
