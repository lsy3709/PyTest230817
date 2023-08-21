from tkinter import *
window = Tk()

# 기본 문법 : + concatate: 연결, * : 반복
btnList = [""] * 3
print(f"btnList 결과 : {btnList}")

# 리스트의 요소로 , 버튼이라는 각 인스턴스 가지고 있다.
# str -> 문자열로 변환하는 함수.
for i in range(0, 3):
    btnList[i] = Button(window, text="버튼" + str(i + 1))

for btn in btnList:
    # btn.pack(side=RIGHT)
    # btn.pack(side = TOP)
    # btn.pack(side = BOTTOM)
    # btn.pack(side = TOP, fill = X)
    # btn.pack(side = TOP, fill = X, padx = 10, pady = 10)
    btn.pack(side=TOP, fill=X, ipadx=10, ipady=10)
    # btn.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)

window.mainloop()
