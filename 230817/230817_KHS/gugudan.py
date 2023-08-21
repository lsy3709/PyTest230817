# print("구구단 몇 단을 계산할까?")
# user_input = input()
# print("구구단", user_input, "단을 계산한다.")
# int_input = int(user_input)
# for i in range(1, 10):
#     result = int_input*i
#     print(user_input, "X", i, "=", result)

# import random
# import time


# def game_gugudan(dans, game_time):
#     print(f'\n{"="*10} 구구단 게임 {"="*10}\n')
#     games = int(input('\n 몇 게임 할까요? : '))  # input 안에서 바로 int 변환

#     games_cnt = 0  # 진행 게임수
#     correct_cnt = 0  # 맞은 게임수
#     incorrect_cnt = 0  # 틀린 게임수
#     g_time = game_time  # 제한시간(초) 설정

#     while games_cnt < games:  # games_cnt가 games보다 작을 때까지 반복
#         dan = random.randint(2, dans)
#         number = random.randint(2, 9)

#         start = time.time()
#         answer = input(f'\n#{games_cnt + 1} 게임: {dan} X {number} = ')
#         end = time.time()

#         if not answer.isdigit():
#             incorrect_cnt += 1
#             print('오입력, 틀렸습니다!')
#         elif (end - start) > g_time:
#             incorrect_cnt += 1
#             print(f'입력 시간 {g_time}초 경과로 오답 처리합니다.')
#         elif int(answer) == (dan * number):
#             correct_cnt += 1
#             print('맞았습니다!')
#         else:
#             incorrect_cnt += 1
#             print('틀렸습니다!')

#         games_cnt += 1

#     print(
#         f'\n총 {games}게임 중\n맞은 게임수: {correct_cnt}\n틀린 게임수: {incorrect_cnt}\n정확도: {(correct_cnt/games)*100:.1f}%')


# dans = 9  # 단수 (9~19)
# game_time = 5  # 응답 시간 제한(초)
# game_gugudan(dans, game_time)

import tkinter as tk
from tkinter import simpledialog
import random
import time


class GugudanGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("구구단 게임")
        self.root.geometry("400x300")

        self.dans = 9
        self.game_time = 5

        self.start_button = tk.Button(
            root, text="게임 시작", command=self.start_game)
        self.start_button.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.question_label.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def start_game(self):
        games = simpledialog.askinteger("게임 설정", "몇 게임 할까요?")
        if games is not None:  # 사용자가 창을 닫을 때 예외 처리
            correct_cnt, incorrect_cnt = self.play_games(games)
            accuracy = (correct_cnt / games) * 100
            result_text = f"총 {games}게임 중\n맞은 게임수: {correct_cnt}\n틀린 게임수: {incorrect_cnt}\n정확도: {accuracy:.1f}%"
            self.result_label.config(text=result_text)

    def play_games(self, games):
        games_cnt = 0
        correct_cnt = 0
        incorrect_cnt = 0
        g_time = self.game_time

        while games_cnt < games:
            dan = random.randint(2, self.dans)
            number = random.randint(2, 9)

            self.question_label.config(text=f"{dan} X {number} = ")

            start = time.time()

            answer = self.show_question(dan, number)

            end = time.time()

            if answer is None:
                break  # 사용자가 대화상자를 닫았을 때

            if not answer.isdigit():
                incorrect_cnt += 1
            elif (end - start) > g_time:
                incorrect_cnt += 1
            elif int(answer) == (dan * number):
                correct_cnt += 1
            else:
                incorrect_cnt += 1

            games_cnt += 1

        self.question_label.config(text="")  # 문제 표시 레이블 초기화
        return correct_cnt, incorrect_cnt

    def show_question(self, dan, number):
        question = f"{dan} X {number} = "
        answer = simpledialog.askstring("구구단 문제", question)
        return answer


if __name__ == "__main__":
    root = tk.Tk()
    app = GugudanGameGUI(root)
    root.mainloop()
