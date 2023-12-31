from collections import defaultdict, OrderedDict

text = '''
이데일리TV 문다애 기자 기술유출이 계속되면 세계 최고 반도체 기술을 보유한 삼성의 미래에도 심각한 악영향을 미칠 수 있습니다. 반도체는 국가 핵심기술인 만큼 국가 경쟁력에도 타격을 줄 우려가 큽니다.
삼성전자 정보보호센터 김성원(가명) 부사장은 인터뷰에서 이 같이 말했다. 삼성전자의 정보보호센터는 삼성전자의 정보보안을 책임지는 핵심 조직이다. 김 부사장은 이 센터의 최고 책임자다.
삼성전자 보안 최고 책임자가 언론과 인터뷰한 것은 이번이 처음이다. 보안 최고 책임자 신원이 대외적으로 노출되면 정보보호 업무에 지장을 줄 수 있어 인터뷰는 익명으로 공개한다.
기술유출 10곳중 9곳은 중국..삼성전자 주타깃
국가정보원에 따르면 산업기밀 해외 유출 적발 건수는 2017년부터 지난해까지 최근 6년간 총 117건에 달한다. 매달 1.6건 꼴이다. 그 중 36건은 ‘국가 핵심 기술’ 유출 사례였다. 법무부에 따르면 전체 기술 유출 사례 중 92.3%는 중국기업들이 연루돼 있는 것으로 나타났다.
이들의 주요 타깃은 삼성전자다. 후발주자인 중국기업들은 세계 최고 수준인 삼성전자의 반도체 기술을 호시탐탐 노리고 있다.
사례는 부지기수다. 삼성전자에서 반도체 업무를 담당하던 직원이 이직을 위해 최신 반도체 초미세 공정과 관련된 국가핵심기술 및 영업비밀 등이 담긴 파일들을 유출하다가 적발됐다. 이 직원이 빼돌리다 적발된 자료에는 삼성전자와 대만 TSMC 두 기업만 대량생산에 성공한 최첨단 3나노 공정 기술이 포함돼 있었다.
최근에는 삼성전자 출신 전직 임원이 반도체 생산라인의 공정 배치도와 설계도면 등을 중국 기업에 유출한 혐의로 기소돼 재판이 진행중이다.
삼성전자 뿐 아니라 계열사나 협력사가 보유한 기술이 타깃이 되기도 한다. 지난해 5월에는 삼성전자 계열 장비회사 ‘세메스’에서 반도체 세정 장비 기술을 빼돌린 연구원들이 적발됐다.
'''.split()

word_count = defaultdict(lambda : 0)


for word in text:
    word_count[word] += 1
  
    

  
test= OrderedDict(sorted(word_count.items(),key=lambda t:t[1], reverse=True)[:10])
print(f"{test}") 
    