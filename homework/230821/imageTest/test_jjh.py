from tkinter import *

## 함수 선언 부분 ##


def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')
    # 파일을 받음
    for i in range(0, XSIZE):
        tmpList = []
        tmpList2 = []
        # 0 ~ 255 라인
        for k in range(0, YSIZE):
            # 각 라인의 0 ~ 255 칸 입력
            # 1바이트씩 받아서 입력함
            # ord -- 각 값의 유니코드를 반환해줌
            # 이 유니코드를 tmpList에 받음
            # cf. 1바이트 .==. 1픽셀
            tempdata = fp.read(1)
            data = int(ord(tempdata))
            tmpList.append(data)
            tmpList2.append(tempdata)
        # 한 라인의 rgb 값을 inImage에 넣어줌
        inImage.append(tmpList)
        #print(f"{i}번째 rgb값 리스트 -- {tmpList}")
        #print(f"{i}번째 유니코드리스트 -- {tmpList2}")
    fp.close()


def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)  # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)


## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []  # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image=paper, state="normal")

# 파일 --> 메모리
# C:/CookAnalysis/RAW/tree.raw
#filename = 'C:\우재남-소스-IT CookBook, 파이썬 데이터 분석 for Beginner-/RAW/tree.raw'
filename = 'D:\내파일/국비교육/우재남-소스-IT CookBook, 파이썬 데이터 분석 for Beginner-/RAW/tree.raw'
loadImage(filename)

# 메모리 --> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()
