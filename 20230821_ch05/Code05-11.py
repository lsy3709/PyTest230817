from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료")

fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label="파일2", menu=fileMenu2)
fileMenu2.add_command(label="열기")
fileMenu2.add_separator()
fileMenu2.add_command(label="종료")

window.mainloop()
