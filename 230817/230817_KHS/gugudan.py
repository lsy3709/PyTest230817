print("구구단 몇 단을 계산할까?")
user_input = input()
print("구구단", user_input, "단을 계산한다.")
int_input = int(user_input)
for i in range(1, 10):
    result = int_input*i
    print(user_input, "X", i, "=", result)

# def game_gugudan(dans, game_time):
#     print(f'\n{"="*10} 구구단 게임 {"="*10}\n')
#     games = input('\n 몇 게임 할까요? : ')

#     games = int(games) # 실행 게임수 설정
#     games_cnt = 0 # 진행 게임수
#     correct_cnt = 0 # 맞은 게임수
#     incorrect_cnt = 0 # 틀린 게임수
#     game_time = game_time # 제한시간(초) 설정

#     while True:
#         dan = random.randint(2, dans)
#         number = random.randint(2,9)

#         if games_cnt == games:
#             print(f'\총  {games}게임 중 \n맞은 게임수: {correct_cnt}\n 틀린 게임수:
#                   {incorrect_cnt}\n정확도: {(correct_cnt/games)*100:.1f}%')
#     break

#     start = time.time
