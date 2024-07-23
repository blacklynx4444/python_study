import random

print("로또 번호 자동 추첨기")
while True:
  try:
    n = input("추첨 횟수 입력 -> ")
    l = int(n)
    if(l <= 0):
      print("0보다 큰 수를 입력하시기 바랍니다.")
    for i in range(l):
      lotto = list(random.sample(range(1, 46), 6))
      lotto.sort()
      print(lotto)
  except:
    print("ERROR")