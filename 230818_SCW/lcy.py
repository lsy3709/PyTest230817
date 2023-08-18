l=open("./230818_SCW/lyrics.txt",'r',encoding="UTF8")
lrc=l.readlines()
print(lrc)

content=""
for line in lrc:
    content=content+line.strip()+"\n"
Num_lrc=content.count("내")
print(f"가사에 나온 '내' 횟수:{Num_lrc}")
