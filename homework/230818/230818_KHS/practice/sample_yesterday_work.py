# 파일 입출력에서, 가사 문서를 입력해서(인코딩 타입: ㅕㅅㄹ-8)
# 메모리상에 f 인스턴스
f = open("./homework/230818/230818_KHS/yesterday.txt", "r", encoding='utf-8')
# f 인스턴스에 들어 있는 문장들을 readline 함수를 이용해서 한번에 다 읽고
yesterday_lyric = f.readlines()
print(yesterday_lyric)
# 파일을 읽어서
f.close()

# contents : 임시 문자열 변수에
contents = ""
# 반복문으로 가사 중에서, 한 라인씩 읽어서
# 공백 제거하고 한줄을 contents 붙이는 반복작업
for line in yesterday_lyric:
    contents = contents+line.strip() + "\n"
    # 디버깅으로 하나씩 출력해서 확인
print(f"contents의 내용이 궁금하면 반복문 안의 내용 : {contents}")
# contents 에서 YESTERDAY 갯수를 다 찾음
result = contents.upper().count("YESTERDAY")
print("Number of a Word 'Yesterday'", result)
