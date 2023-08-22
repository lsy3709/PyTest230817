from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)

window.mainloop()
