from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##


def func_open():
    # askopenfilename , 이미지 파일 선택.
    filename = askopenfilename(parent=window, filetypes=(
        ("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    # 불러온 이미지 PhotoImage를 통해서, 임시 메모리 잠시 가지고 있음.
    photo = PhotoImage(file=filename)
    # pLabel 라벨 붙이기.
    pLabel.configure(image=photo)
    pLabel.image = photo


def func_exit():
    window.quit()
    window.destroy()


## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
