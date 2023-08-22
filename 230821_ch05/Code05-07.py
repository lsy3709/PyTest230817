from tkinter import *
from tkinter import messagebox
# 윈도우창 인스턴스.
window = Tk()

## 함수 선언 부분 ##


def myFunc():
    # chk 인스턴스에 속성의 값을 가지고 와서 분기. 상태 변수 이용해서,
    if chk.get() == 0:
        print(f"chk 의 값 조회 : {chk.get()}")
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        print(f"chk 의 값 조회 : {chk.get()}")
        messagebox.showinfo("", "체크버튼이 켜졌어요.")


## 메인 코드 부분 ##
# IntVar() 의 기본값 : 0
chk = IntVar()
# 해당 Checkbutton , variable -> chk
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)

cb1.pack()

window.mainloop()
