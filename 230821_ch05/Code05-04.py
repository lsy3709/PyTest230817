from tkinter import *
window = Tk()
# PhotoImage 사진 이미지를 불러오는 역할. gif 형식으로 불러옴.

photo = PhotoImage(file="gif/dog13.gif")
# 불러온 이미지를 라벨의 이미지 속성에 붙여 넣기.
label1 = Label(window, image=photo)

# 해당 라벨, 윈도우창에 붙이기.
label1.pack()

window.mainloop()
