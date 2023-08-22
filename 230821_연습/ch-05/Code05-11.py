from tkinter import *
# 메인 메뉴의 부모창
window = Tk()

# 파일 메뉴의 부모창 mainMenu
mainMenu = Menu(window)


window.config(menu=mainMenu)


fileMenu = Menu(mainMenu)
fileMenu2 = Menu(mainMenu)

mainMenu.add_cascade(label="파일", menu=fileMenu)
mainMenu.add_cascade(label="파일2", menu=fileMenu2)

fileMenu.add_command(label="열기")
fileMenu2.add_command(label="열기2")

fileMenu.add_separator()

fileMenu.add_command(label="종료")
fileMenu2.add_command(label="종료2")

window.mainloop()
