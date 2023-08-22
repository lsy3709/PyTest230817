# 파일 입출력에서, 가사 문서를 입력해서(인코딩 타입: utf-8)
# 메모리상에 f 인스턴스에 있음.
f = open("./PyTest230817/230818/yesterday_utf8.txt", 'r', encoding='utf-8')
# f 인스턴스에 들어 있는 문장들을 ,readlines 함수를 이용해서, 한번에 다 읽고.
yesterday_lyric = f.readlines()
# 파일의 내용을 잘 읽었는지 확인 하는 부분.
# 파일을 잘 읽어서, yesterday_lyric 담아서, 해당 인스턴스를 반납.
f.close()

# contents : 임시 문자열 변수에
contents = ""
# 반복문으로 가사 중에서, 한 라인씩 읽어서
# 공백 제거하고 한줄을 contents 붙이는 반복작업
for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"
    # 디버깅으로 하나씩 출력 부분으로 보여드리고, 확인.
    # print(f"contents의 내용이 궁금 하면 반복문 안의 내용 : {contents}")
juke = "true"

# 콘솔 부분
print("🎺")
while(juke):
   print("1번 : 노래제목 \n2번 : 가사 전체 보기\n3번 : 가사 갯수 찾기\nx: 종료")
   a = input()
   if a == "1" :
      print("노래 제목 : yesterday")
   elif a == "2" :
      print(contents)
   elif a == "3" :
      print("검색할 가사 입력 ex) yesterday ")
      b = input()
      count = contents.lower().count(b.lower())
      print(f"{count}개")
   elif a == "x" : break
   else: print()
print("끝")

# print(f"contents의 내용이 궁금 하면 반복문 다 종료후 : {contents}")
# #   contents 에서 YESTERDAY 갯수를 다 찾음.
# result = contents.upper().count("YESTERDAY")
# print(f"가사 중에 yesterday 를 대문자로 변환 후 갯수 찾은 결과: {result}")
