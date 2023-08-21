from tkinter import *
from tkinter.filedialog import *

## 함수 정의 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="선택된 파일 이름")
label1.pack()

# 윈도우에서 탐색기, 특정의 파일을 열기 나타는 시스템의 파일 탐색창.
filename = askopenfilename(parent=window, filetypes=(
    ("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
# filename 절대 경로를 문자열로 변환 해서, 라벨지에 출력하기.
label1.configure(text=str(filename))

window.mainloop()
