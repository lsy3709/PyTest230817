with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp:
    with open("C:/CookAnalysis/CSV/new_singer230822.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(',')
        # map 함수는 첫번째 str 함수: 문자열로 변경하는 함수/ 두번째 인자 header_list의 요소를 하나씩 거내서 문자열화/ 마지막 join함수를 이용해서 콤마로 함치기
        header_str = ','.join(map(str, header_list))
        # print(f"head_str: {header_str}")

        # csv에 쓰는 작업, outFp 인스턴스를 이용해서 쓰기 작업 수행.
        # 첫행의 컬럼을 먼저 쓰기 작업
        # inFP: csv 파일 내용을 담고 있는 인스턴스
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')

            row_list[-1] = row_list[-1].replace('.', '/')
            height_str = "{0:.2f}".format(int(row_list[-2]))

            row_list[-2] = height_str
            row_str = ','.join(map(str, row_list))
            outFp.write(row_str + '\n')

print('Save. OK~')
