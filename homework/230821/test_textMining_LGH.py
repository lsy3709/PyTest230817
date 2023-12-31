from collections import defaultdict, OrderedDict

text = '''
"다음 달 청와대에서 선우예권과 사무엘 윤 등 정상급 K-클래식 주자들이 참여하는 공연이 열린다.
문화체육관광부는 국립심포니오케스트라, 국립오페라단과 함께 
9월 9일 오후 7시 30분과 10일 오후 5시에 청와대 헬기장에서 
K-클래식 공연 ‘2023 블루하우스 콘서트(Blue House Concert)’를 개최한다고 21일 밝혔다.
9월 9일에는 K-클래식과 국악, K팝이 어우러진 오케스트라 공연이 펼쳐진다.
광주시립교향악단 홍석원 상임 지휘자와 국립심포니오케스트라가 차이콥스키의 ‘예브게니 오네긴’ 
중 폴로네즈를 연주한다. 이후 브람스 ‘헝가리 춤곡 5번’, 차이콥스키 ‘호두까기 인형’ 등
친숙한 클래식 음악을 선보인다.
특히 라흐마니노프 ‘파가니니 주제에 의한 랩소디’는 
한국인 최초로 2017년 ‘반 클라이번 콩쿠르’에서 우승한 피아니스트 선우예권과 협연한다.
소리꾼 고영열의 ‘북’과 K팝 그룹 마마무의 솔라·문별의 공연도 가세한다.
10일에는 사무엘 윤, 이아경, 양준모, 임세경 등 한국을 대표하는 성악가들이 총출동한다.
로시니 ‘세비야의 이발사’, 푸치니 ‘나비부인’ 등 유명 오페라의 아리아와 함께,
‘산촌’, ‘신고산 타령’ 등 매력적인 우리 가곡도 울려 퍼진다.
서울대학교 장윤성 교수 지휘로 국립심포니오케스트라와 한국입양어린이합창단(단장 김수정)이 함께
‘아리랑’과 ‘넬라 판타지아’를 공연한다.
이번 콘서트는 ‘2018 평창동계올림픽’ 개회식을 총연출했고,
최근 현대적으로 재해석한 고전 연극 ‘파우스트’연출로 호평받은 양정웅 연출가가 맡는다.
이번 행사도 미디어아트와 레이저쇼 등 역동적인 무대 연출로 예술과 기술,
클래식과 대중가요가 함께하는 새로운 시도를 한다.
국립현대미술관 전시 등에 참여했던 빠키(VAKKI) 작가와 한요한 작가가 미디어아트에 참여한다.
이번 콘서트는 사전에 공연 관람을 신청하면 누구나 무료로 볼 수 있다.
23일 오전 10시부터 1인당 최대 4장까지 인터파크에서 접수(예매수수료는 2000원)하면 된다.
단 야외 공연 특성상 우천 시 취소될 수 있다.
문체부는 지난해 청와대 개방이후 다양한 공연을 펼친 데 이어 
올가을에도 10월까지 국악과 국악관현악 등 다양한 장르의 야외 공연을 이어갈 예정이다."
'''.lower().split()

word_count = defaultdict(lambda : 0)

for word in text :
    word_count[word] += 1

test_OrederedDict = OrderedDict(sorted(word_count.items(), key=lambda t: t[1],
                                       reverse=True)).items()
# print(f"전체 : {test_OrederedDict}")
for idx, (i, v) in enumerate(test_OrederedDict, 1) :
    print(f"단어 : {i}, 횟수 : {v}")
    if idx == 10:
        break