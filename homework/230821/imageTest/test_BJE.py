from tkinter import *

## 함수 선언 부분 ##
def loadImage(fname) :
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    # 함수 해당 파일명을 매개변수로 지정
    # 'rb' -> 이진값으로 읽겠다


    # fp, 인스턴스에서, 해당 이미지의 내용이 담겨있음
    for i in range(0, XSIZE) :
        # 순서1
        tmpList = []
        # 순서2
        for k in range(0, YSIZE) :
            # fp.read(1) -> 이미지의 한 바이트를 읽기 한픽셀
            # ord -> 해당 픽셀의 값을 유니코드의 값으로 리턴
            # int -> 정수화
            # data : 한 픽셀에 있는 RGB 값을 의미
            data = int(ord(fp.read(1)))
            # tmpList 임시리스트에 추가
            tmpList.append(data)
            # 순서3
            # inImage : 메모리 상에 있는 이미지의 rgb 값을 
            # 256 x 256, 2차원 리스트 형식으로 되어있음
            # inImage 아래에 전역으로 선언
            
        inImage.append(tmpList)
        
       
        
        # ord(fp.read(1))
        # print(f"ord(fp.read(1)): {ord(fp.read(1))}")
    fp.close()
    # inImage
    # print(f"inImage: {inImage}")
    
    

    # print(f"{data}")
    # tmpList
    # print(f"{tmpList}")
# 메모리 상에 있는 이미지의 이차원 배열을 출력하는 부분
def displayImage(image) :
    # 전역으로, 가로 세로 256으로 설정
    global XSIZE, YSIZE
    # rgbString : RGB 코드를 문자열 출력하는 부분
    rgbString = ""
    # 가로의 0행일때
    for i in range(0, XSIZE) :
        tmpString = ""
        # 임시로 RGB 값을 담을 문자열
        for k in range(0, YSIZE) :
            # 0행일때, 0열 ~255열까지의 값을 반복문
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한칸 공백
        rgbString += "{" + tmpString +  "} " # } 뒤에 한칸 공백
        
    paper.put(rgbString)
    
    # image[i][k]
    # print(f" data = image[i][k]: {image[i][k]}")

    # tmpString
    # print(f"tmpString: {tmpString}")

    # rgbString
    # print(f"rgbString: {rgbString}")
  
    

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE=256,256
inImage=[] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

# 파일 --> 메모리
filename = 'RAW/tree.raw'  # C:/CookAnalysis/RAW/tree.raw
loadImage(filename)

# 메모리 --> 화면 
displayImage(inImage)

canvas.pack()
window.mainloop()
