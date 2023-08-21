f = open("./homework/230818/eunseongzzangzzangman/thefox_utf8.txt", 'r', encoding='utf-8')
thefox_utf8 = f.readlines()
print(f"thefox_utf8의 내용 출력 부분 : {thefox_utf8}")
f.close()

contents = ""
for line in thefox_utf8:
    contents = contents + line.strip() + "\n"

print(f"contents의 내용이 궁금 하면 반복문 다 종료 후 : {contents}")

result = contents.upper().count("KAKA")
print(f"가사 중에 kaka를 대문자로 변환 후 갯수 찾은 결과 {result}")
