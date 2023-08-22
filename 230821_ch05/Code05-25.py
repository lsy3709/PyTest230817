from tkinter import *

## 함수 선언 부분 ##

# 함수 해당 파일명을 매개변수로 지정해서.
# 'rb' -> 이진값으로 읽겠다.

# 이미지를 읽어서 -> 메모리 임시 저장.


def loadImage(fname):
    global inImage, XSIZE, YSIZE
    # rb -> 이진값으로 읽는다. b 가 없다면, 기본 문자열로 읽는다.
    # inputStream , fileInputStream,
    fp = open(fname, 'rb')

    # fp , 인스턴스에서, 해당 이미지의 내용이 담겨 있음.
    for i in range(0, XSIZE):
        # 순서1
        tmpList = []
        # 순서2
        # 0 ~ 255 까지, 256 제외.
        for k in range(0, YSIZE):
            # fp.read(1) -> 이미지의 한 바이트를 읽기. 한픽셀
            # ord -> 해당 픽셀의 값을 유니코드의 값으로 리턴
            # int -> 정수화
            # data : 한 픽셀에 있는 RGB 값을 의미.

            # print(f"fp.read(1) : {fp.read(1)}")
            # 결과 fp.read(1) : b'\x86'

            # print(f"ord(fp.read(1)) : {ord(fp.read(1))}")
            # 결과 ord(fp.read(1)) : 77

            data = int(ord(fp.read(1)))
            # print(f"data의 값: {data}")
            # 결과 : data의 값: 62

            # tmpList 임시리스트에 추가.
            tmpList.append(data)
            # print(f"tmpList 결과: {tmpList} ")
            # tmpList 결과: [84, 84, 83, 82, 82, 82, 83, 83, 84, 84, 82, 79, 78, 75, 74, 73, 69, 68, 66, 66, 67, 68, 67, 65, 63, 62, 61, 61, 62, 67, 70, 75, 82, 88]
        # 순서3
        # inImage : 메모리 상에 있는 이미지의 rgb 값을
        # 256x 256 , 2차원 리스트 형식으로 되어 있음.
        # inImage 아래에 전역으로 선언.
        # 함수 실행하면, 전역에 이미지의 값이 이중 리스트로
        # 뒤어 가고, 이제 출력 할 예정.
        inImage.append(tmpList)
        # print(f"inImage 의 값: {inImage}")
        # 결과 -> [ [],[],[],....[]  ] -> 256x 256

    fp.close()

# 메모리 상에 있는 이미지의 이차원 배열을 출력하는 부분.


def displayImage(image):
    # 전역으로, 가로 세로 256으로 설정.
    global XSIZE, YSIZE
    # rgbString : RGB 코드를 문자열 출력하는 부분.
    rgbString = ""
    # 가로의 0행 일때
    for i in range(0, XSIZE):
        # 임시로 RGB 값을  담을 문자열
        tmpString = ""
        # 0행 일 때, 0열 ~ 255열 까지의 값을 반복문.
        for k in range(0, YSIZE):
            # 각 픽셀의 RGB 값.
            data = image[i][k]
            # print(f"data 의 값: {data}")
            # 결과 data 의 값: 69 샘플.

            # %02x -> 16진수 표기법.
            tmpString += "#%02x%02x%02x " % (data, data, data)  # x 뒤에 한칸 공백
            # print(f"tmpString 의 값: {tmpString}")
            # 결과 : tmpString 의 값: #555555 #565656 #565656 #555555 #565656 #555555 #565656 #565656 #565656 #545454 #525252 #505050 #4d4d4d #4a4a4a #484848 #474747

        # 전체 rgb 문자열 값이 나옴.
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
        # print(f"rgbString 의 값: {rgbString}")
        # 결과 샘플 : #6f6f6f #707070 연속으로 들어가 있는 구조.
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
# raw 확장자 이미지는 , 일반 이미지랑 다르고,
# 테스트 용 만들어진 흑백 사진이다.
# filename = 'RAW/tree.raw'
filename = 'RAW/cat256.raw'
loadImage(filename)

# 메모리 --> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()
