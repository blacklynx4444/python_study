# 생성함수
# list, tuple, set

li = [1, 2, 3, 4, 5, 6] # 대괄호는 list
print(li)
print('리스트 첫 번째 : '+str(li[0]))
l = len(li)
print('리스트 길이 : '+str(l))

for i in range(l):
  print(li[i])

# 리스트 슬라이싱
print(li[0:3])
print(li[::2])  # 시작 인덱스 생략은 처음부터 :끝 인섹스 생략은 끝까지 2개 간격으로
print(li[0:-2]) # 

tu = (1, 2, 3, 4, 5, 6) # 소괄호는 tuple

se = {1, 2, 3, 4, 5, 6} # 중괄호는 set. set은 순서가 뒤바낄 수 있다. 또한 중괄호 초기화 불가.

print('튜플은 수정이 불가하다.')

d = {1:10}