import csv
# csv 파일 두개를 합치는 예제
with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA:
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum_230822.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)

            # 2개의 csv 파일의 구조가 동일해서 하나로 덮어쓰기
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # cvs 파일을 쓰는 작업
            csvWriter.writerow(header_list)

            # 2 행부터 실제 데이터 값 쓰기
            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')
