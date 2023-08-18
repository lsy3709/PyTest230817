f = open("./homework/230818/YEY/leesuyoung.txt", 'r', encoding='utf-8')
like_lyric = f.readlines()
# print(f"파일 읽어 오기 : {yesterday_lyric}")
f.close()

contents = ""
for line in like_lyric:
    contents = contents + line.strip() + "\n"

    # print(contents)
count = contents.count("얼마나")

print(f"가사중에 [얼마나] 갯수 찾은 결과 : {count}")