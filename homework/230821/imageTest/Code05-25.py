from tkinter import *

## 함수 선언 부분 ##
# 매개변수 : 파일명
def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    # fp : 해당 이미지의 내용이 저장
    fp = open(fname, 'rb')

    '''해당 이미지의 가로, 세로 픽셀의 수 / 즉 해당 이미지의 크기 만큼 반복을 한다.'''
    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :

            '''이미지에서 byte로 읽는다.
            ord() : 읽은 1byte[fp.read(1)]의 유니코드 값 리턴
            data : 한 픽셀의 rgb값'''
            data = int(ord(fp.read(1)))
            # print(f"ord(fp.read(1)) 데이터 : {ord(fp.read(1))}")
            # print(f"data 의 값 : {data}")

            tmpList.append(data)
            # print(f"tempList 의 데이터 : {tmpList}")

        '''inImage : 메모리상에 있는 이미지의 rgb 값
            256 X 256, 2차원 리스트의 형식'''
        inImage.append(tmpList)
        # print(f"tempList 의 데이터 타입 : {tmpList[:]}")
        # print(f"inImage 의 데이터 타입 : {type(inImage)}")
        # print(f"inImage 의 데이터 값 확인 : {inImage[:]}")        

    fp.close()

'''이미지의 2차원 배열을 출력
    tmpString : 임시로 rgb 값을 담을 문자열'''
def displayImage(image) :
    global XSIZE, YSIZE
    rgbString = ""

    '''0행 ~ 255행 , 0열 ~ 255열
        [0행][0열].........[255행][255열]을 나타내는 반복문'''
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            '''각 픽셀의 rgb 값'''
            data = image[i][k] 
            '''%02x : 16진수 표기법'''
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백
            # print(f"tmpString 데이터 확인하기 ================================ : {tmpString}")
        rgbString += "{" + tmpString +  "} "  # } 뒤에 한칸 공백
        # print(f"rgbString 데이터 확인하기 =================================== : {rgbString}")

    paper.put(rgbString)
    # print(f"rgbString 데이터 타입 : {type(rgbString)}")

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE=256,256
inImage=[] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
'''해당 사진을 불러와서 paper에 저장'''
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# 파일 --> 메모리
filename = 'RAW/tree.raw'  # C:/CookAnalysis/RAW/tree.raw
'''읽은 파일을 메모리상에 올림'''
loadImage(filename)

# 메모리 --> 화면 
displayImage(inImage)

canvas.pack()
window.mainloop()
