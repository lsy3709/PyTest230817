from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
# messagebox 다이얼로그 창. alert 창. 토스트 창.


def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")


## 메인 코드 부분 ##
window = Tk()

# 사진 불러오기.
photo = PhotoImage(file="gif/dog10.gif")
# 이미지 버튼, 이미지를 추가했음. 이벤트 핸들러도 추가.
button1 = Button(window, image=photo, command=myFunc)

# 윈도우창에 버튼 붙이기.
button1.pack()

# 그려주기.
window.mainloop()
