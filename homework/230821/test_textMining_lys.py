from collections import defaultdict, OrderedDict

text='''
"축구 슈퍼스타 리오넬 메시가 지난 6월 프랑스 파리 생제르맹을 떠나 미국 인터 마이애미로 이적한 이후 티켓 가격이 천정부지로 치솟고 있다.
20일(현지시간) CNBC는 메시 이적 이후 미국 내 시즌 후반 경기 티켓 가격이 중고시장에서 전년 대비 1700% 이상 급등했다고 보도했다.
CNN은 메시가 지난달 인터 마이애미와 연간 5000만~6000만 달러 규모의 계약을 체결했고 팀 지분도 포함돼 있다고 전했다.
메시의 미국 진출로 미국 프로축구 리그인 메이저리그 사커(MLS)에 대한 관심이 급증하는 가운데 홈 경기와 원정 경기의 티켓 가격이 고공행진하고 있다.
CNBC는 티켓IQ 데이터를 인용해 홈 경기의 경우 중고거래의 평균 가격이 메시 영입 전 152달러에서 864달러로 468%(18일 기준) 올랐다고 전했다.
뉴욕과 로스앤젤레스 등 대도시가 포함된 원정 경기 티켓 가격은 더 뛴 것으로 나타났다.
CNBC는 “나머지 모든 원정 경기의 평균 티켓 가격은 작년 대비 1002%(15일 기준) 올랐다”고 전했다.
이번 시즌 인터 마이애미의 남은 경기 티켓 구하기도 ‘하늘의 별 따기’가 됐다. CNBC는 다가오는 뉴욕 레드불스와의 경기의 경우 평균 티켓 가격이 작년 90달러에서 올해 1674달러로 1760% 급등했다고 전했다.
라이벌 팀인 올랜도 시티 SC와의 경기의 평균 티켓 가격도 작년 97달러서 올해 메시 합류 이후 1755달러로 치솟아 1709% 올랐다.
저렴한 좌석 가격도 뛰었다. 뉴욕 레드불스와의 경기의 가장 저렴한 티켓은 메시의 합류로 36달러에서 578달러까지 올랐다고 CNBC는 전했다.
메시 영입 이후 애플TV의 ‘MLS 시즌패스’ 구독이 두 배로 증가하고 인터 마이애미 인스타그램 계정 팔로워도 100만명에서 1400만명으로 늘었다."
'''.split()

word_count = defaultdict(lambda : 0)
for word in text:
    word_count[word] += 1 

test_OrderedDict = OrderedDict(sorted(word_count.items(),key=lambda t:t[1],
                                      reverse=True)).items()

print(f"test_OrderedDict의 결괏값 전체: {test_OrderedDict}")

for i,v in test_OrderedDict:
    print(f"test_OrderedDict의 결괏값 : key:{i}, value:{v}")

print("")


q=1
print("------------빈도수 TOP10-----------")
top_items = list(test_OrderedDict)[:10]
for word, count in top_items:
    print(f"Top{q} : {word}  ({count}회)")
    q +=1



