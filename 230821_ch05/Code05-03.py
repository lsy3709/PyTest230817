from tkinter import *
# 윈도우 창을 그려주는 인스턴스
window = Tk()

# 라벨이라는 클래스에서, 속석으로, text 속성을 사용하면,
label1 = Label(window, text="COOKBOOK. 데이터 분석을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
# anchor=SE -> S: south , E: east
label3 = Label(window, text="공부 중입니다.", bg="magenta",
               width=20, height=5, anchor=SE)

# 윈도우 창에 붙이는 작업.
label1.pack()
label2.pack()
label3.pack()

window.mainloop()
