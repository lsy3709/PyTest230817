# 파일, 읽기, 쓰기
# 파일 읽기.
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp:
    # 파일 쓰기.
    with open("C:/CookAnalysis/CSV/new_singer230822.csv", "w") as outFp:
        # inFp :csv 파일을 읽은 내용을 담은 임시 인스턴스, 한줄 읽기
        header = inFp.readline()
        # header 에서 공백제거
        header = header.strip()
        # header 라는 리스트를 콤마를 구분자로 해서, 분리.
        header_list = header.split(',')
        # map 함수라는 첫번째 str 함수 : 문자열로 변경하는 함수
        # 두번째 인자 header_list 리스트의 요소를 하나씩 꺼내서 문자열화
        # 마지막 join 함수를 이용해서 콤마로 합치기.
        header_str = ','.join(map(str, header_list))
        # print(f"header_str 의 출력 :{header_str}")

        # csv 에 쓰는 작업, outFp 인스턴스를 이용해서 쓰기 작업 수행.
        # 첫행의 컬럼을 먼저 쓰기 작업.
        outFp.write(header_str + '\n')
        # 2번째 행부터는 실제 데이터 값을 쓰는 작업.
        # inFp :csv 파일의 내용을 담고 있는 인스턴스
        for inStr in inFp:
            # 한줄씩 읽고, 양쪽 공백 제거
            inStr = inStr.strip()
            # 콤마를 기준으로 나누기.
            row_list = inStr.split(',')
            print(f"row_list 의 출력 :{row_list}")
            # row_list[-1] 리스트의 마지막 부분에  바꾸기 . -> /
            row_list[-1] = row_list[-1].replace('.', '/')
            # row_list[-2] 리스트의 뒤에서 2번째 , 값을 int로 정수화
            # 실수형으로 소수점 2째 자리 확인 필요.
            height_str = "{0:.2f}".format(int(row_list[-2]))
            print(f"height_str 의 출력 :{height_str}")
            # 키 에 값에 소수점으로 표기한 형식으로 재 할당.
            row_list[-2] = height_str
            # row_list 의 요소를 하나씩 꺼내어서 , str 함수를 이용해 문자열화
            # join 함수를 이용해서, 콤마를 기준으로 합치기.
            row_str = ','.join(map(str, row_list))
            # 해당 csv 파일에 쓰는 작업.
            outFp.write(row_str + '\n')

print('Save. OK~')
