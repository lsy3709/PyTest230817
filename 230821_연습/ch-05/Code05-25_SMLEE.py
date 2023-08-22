from tkinter import *

## 함수 선언 부분 ##

# 메모리 -> 출력함수


def loadImage(fname):
    global inImage, XSIZE, YSIZE
    # rb -> read byte 이진값으로 읽는다. b가 없으면 기본 문자열로 읽는다.
    # inputStream, fileInputStream
    fp = open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
            # 출력 data = int(ord(fp.read(1)))
            # print(f'data 값: {data}')
            print(f"fp.read(1) : {fp.read(1)}")
            # print(f"ord(fp.read(1)) : {ord(fp.read(1))}")
        inImage.append(tmpList)
        # 출력 tmpList
        print(f'tmpList: {tmpList}')

    fp.close()
    # 출력 inImage
    print(f'inImage: {inImage}')


def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)  # x 뒤에 한칸 공백
        # 출력 tmpString
        print(f'tmpString: {tmpString}')
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
        # 출력 rgbString
        print(f'rgbString: {rgbString}')
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
filename = 'RAW/tree.raw'  # C:/CookAnalysis/RAW/tree.raw
print(f'파일명: {filename}')
loadImage(filename)

# 메모리 --> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()

# ord(ft.read(1)) 값 출력
ft = open(filename, 'rb')
byte_value = ft.read(1)
ascii_value = ord(byte_value)
print(f'ord(byte_value)의 ASCII 값: {ascii_value}')

ft.close()
