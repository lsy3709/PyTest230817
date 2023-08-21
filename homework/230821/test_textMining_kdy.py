from collections import defaultdict, OrderedDict

#https://n.news.naver.com/mnews/article/092/0002302448?sid=105

text = '''

"삼성전자는 이미 스마트폰에 사용된 알루미늄 중 가장 강력한 ‘아머 알루미늄’을 채택했는데,
내년에 나올 갤럭시S24 울트라에는 티타늄 소재를 채택해 전작보다 무게가 더 가벼워질 것으로 보인다.
티타늄 프레임은 올해 애플이 아이폰15 프로 모델에 적용할 것으로 예상되고 있다.
공개된 영상에서 갤럭시S24울트라의 테두리는 전작과 달리 다소 둥근 곡선형을 하고 있다. 
후면 카메라는 전작 그대로 4개의 물방울 렌즈가 탑재되나 좌측의 카메라 렌즈들은
전작과 달리 세로로 긴 타원형이 둘러싼 섬 형태의 디자인을 채택했다.
또, 3배 줌 망원 렌즈가 전작의 1000만 화소보다 5배 높은 5000만 화소로 바뀔 것으로 전망됐다.
화면 크기는 0.1인치 늘어나 6.9인치가 될 예정이며, OLED 패널은 144Hz 화면 주사율을 지원하고
퀄컴 스냅드래곤 8 젠 3, 16GB 램, 더 커진 5,500mAh 배터리가 탑재될 예정이다.
4RMD는 갤럭시S24 울트라의 색상이 팬텀 블랙과 팬텀 화이트, 퍼플, 골드 등 4종으로 출시될 것으로 예상했다."
'''.lower().split()

# okt = Okt()
# nouns = okt.nouns(text) # 명사만 추출

# words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

# count = Counter(words)



d = defaultdict(lambda : 0) #Default 값을 0으로 지정

d = defaultdict(list) #Default 값을 list로 지정

for i in range(10) :
    d[i].append(i)   # key : i 인 list에 i 추가
    d[i].append(i*i) # key : i 인 list에 i의 제곱 추가



word_count = defaultdict(lambda : 0)

for word in text:
    word_count[word] += 1

test_OrderedDict = OrderedDict(sorted(word_count.items(), key=lambda t : t[1],
                                          reverse = True)).items()
    
count = 0
for k, v in test_OrderedDict:
  print(k + " : " + str(v) + "개")
  count += 1
  if count == 10:
     break