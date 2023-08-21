from collections import defaultdict as df,OrderedDict as odd

#작은 따옴표3개,큰따옴표 1개로 시작
text='''
"미국의 한 식당에서 밀크셰이크를 먹은 손님 3명이 사망하고 3명이 입원 치료를 받는 일이 발생했다.
20일(현지시각) CNN에 따르면 미국 워싱턴주 보건부는 워싱턴주 타코마의 한 프랜차이즈 햄버거 가게에서 판매된 밀크셰이크에서 리스테리아균 오염이 확인됐다고 밝혔다.
앞서 보건당국은 지난 2월27일에서 지난달 22일 사이 이 식당에서 밀크셰이크를 마신 손님 중 3명이 사망하고 3명이 병원에 입원하자 조사를 벌였다. 그 결과 이 식당의 오래된 아이스크림 기계에서 리스테리아균이 검출됐다.
보건당국은 이 식당의 밀크셰이크가 이들 6명의 리스테리아균 감염을 촉발했다고 보고 있다. 이와 관련 해당 식당 측은 별다른 입장을 밝히지 않았다.
해당 식당은 지난 8일 아이스크림 기계 사용을 중단했으나 리스테리아균의 잠복기가 최장 70일에 달해 피해자가 더 늘 수도 있는 상황이다.
이에 따라 보건당국은 지난 5월29일에서 8월7일 사이 이 레스토랑에서 식사를 한 손님들 중 리스테리아 증상을 보이는 이는 즉시 의료기관에 연락하라고 경고했다.
리스테리아균은 물과 흙에 서식하는 박테리아로, 영하 20도에서도 생존이 가능한 것으로 알려졌다. 미국 질병통제예방센터(CDC)에 따르면 매년 1600명이 리스테리아균에 감염되고 이중 약 260명이 사망한다. 열과 근육통, 설사, 두통 등의 증상이 나타나며 면역력이 약한 노인, 임산부, 유아 등이 취약한 것으로 알려졌다."
'''.lower().split()

newspaper=df(lambda:0)

for word in text:
    #newspaper에 1단식 담기
    newspaper[word]+=1
    
test_OrderedDict=odd(sorted(newspaper.items(),key=lambda t:t[1],
                            reverse=True)).items()
print(f"test_OrderedDict의 전체 값:{test_OrderedDict}")

for i,v in test_OrderedDict:
    if(v<=1):
        continue
    print(f"test_OrderedDict 의 결과값 i:{i},v:{v}")
    