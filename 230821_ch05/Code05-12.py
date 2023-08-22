from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##

# 기본 다이얼로그 창.


def func_open():
    messagebox.showinfo("메뉴 선택", "열기 메뉴를 선택함")


def func_exit():
    window.quit()
    window.destroy()


## 메인 코드 부분 ##
window = Tk()

# 메인 메뉴에 상위 메뉴, 하위메뉴 옵션이 계속 겹침.
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
# command , 버튼에서 이벤트 핸들러 동일. 위에 정의한 함수를 호출.
fileMenu.add_command(label="열기", command=func_open)

fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()
