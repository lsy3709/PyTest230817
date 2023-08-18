
# 구구단

gugudan = "true"

print("===구구단 계산기===")
print("=== 끝내려면 x ===")

while(gugudan):
   print("구구단 몇 단을 계산할까?")
   user_input = input()
   if user_input == "x" : break
   print(f"구구단 {user_input}단")
   int_input = int(user_input)
   for i in range(1,10):
      result = int_input * i
      print(f"{user_input} x {i} = {result}")
print("끝!")