from tkinter import *
window = Tk()

## 함수 선언 부분 ##
# 해당 함수를 이용해서, 상태 값의 조건에 따라서,
# 라벨지 안에 텍스트 내용만 교체하는 중.


def myFunc():
    if var.get() == 1:
        label1.configure(text="파이썬")
    elif var.get() == 2:
        label1.configure(text="C++")
    else:
        label1.configure(text="Java")


## 메인 코드 부분 ##
# IntVar() 기본값 0
# rb1 ~ rb3 : 버튼.
var = IntVar()
rb1 = Radiobutton(window, text="파이썬", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="C++", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="Java", variable=var, value=3, command=myFunc)

# 결과 창 : 빨간색으로 표기 되고 있음.
label1 = Label(window, text="선택한 언어 : ", fg="red")

# 윈도우 창에, 버튼과 결과 라벨을 붙이는 함수., 출력하는 함수.
rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
