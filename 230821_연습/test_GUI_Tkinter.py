import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename()  # 파일 선택 다이얼로그 열기
    if file_path:
        with open(file_path, 'r') as file:
            file_contents.set(file.read())


# GUI 애플리케이션 생성
root = tk.Tk()
root.title("파일 읽기 예제")

file_contents = tk.StringVar()
file_contents.set("파일 내용이 여기에 표시됩니다.")

# 파일 열기 버튼 생성
open_button = tk.Button(root, text="파일 열기", command=open_file)
open_button.pack()

# 파일 내용 표시 레이블 생성
file_label = tk.Label(root, textvariable=file_contents, wraplength=400)
file_label.pack()

root.mainloop()
