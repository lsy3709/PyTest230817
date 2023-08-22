from tkinter import *

# 윈도우 창 부분 인스턴스.
window = Tk()

# 메뉴 부분 구성. mainMenu : 상위 메뉴
mainMenu = Menu(window)
mainMenu2 = Menu(window)
window.config(menu=mainMenu)
window.config(menu=mainMenu2)

fileMenu = Menu(mainMenu)
fileMenu2 = Menu(mainMenu2)
mainMenu.add_cascade(label="파일", menu=fileMenu)
mainMenu2.add_cascade(label="파일2", menu=fileMenu2)
fileMenu.add_command(label="열기")
fileMenu2.add_command(label="열기2")
fileMenu.add_separator()
fileMenu2.add_separator()
fileMenu.add_command(label="종료")
fileMenu2.add_command(label="종료2")

window.mainloop()
