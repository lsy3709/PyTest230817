from tkinter import *

# 윈도우 창 부분 인스턴스.
window = Tk()

# 메뉴 부분 구성. mainMenu : 상위 메뉴
# 메인 메뉴의 부모 창 -> window
mainMenu = Menu(window)
# 틀린 부분, 메인 메뉴는 하나만 있으면 되고, 하위 메뉴를 부모 메뉴에 붙이는 내용.
# mainMenu2 = Menu(window)
window.config(menu=mainMenu)
# 틀린 부분.
# window.config(menu=mainMenu2)

# 파일 메뉴의 부모 창 -> 메인 메뉴
fileMenu = Menu(mainMenu)
# 틀린 부분.
# fileMenu2 = Menu(mainMenu2)
# 수정.
fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
# 틀린 부분 mainMenu2 -> mainMenu
mainMenu.add_cascade(label="파일2", menu=fileMenu2)

# 부모 메뉴 -> 파일1 메뉴
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료")

# 부모 메뉴 -> 파일2 메뉴
fileMenu2.add_command(label="열기2")
fileMenu2.add_separator()
fileMenu2.add_command(label="종료2")

window.mainloop()
