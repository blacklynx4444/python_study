print(bool(0))  #False
print(bool(1))  #True
print(bool(2))  #True
print(bool('')) #False
print("SBS\n아카데미")
single_line = "한 줄의 문자열"
boole = True
print(type(single_line))
print(type(boole))

s = 'hello'
#문자열은 리스트와 동일하게 취급합니다. 그래서 인덱스 번호를 가집니다. 프로그래밍은 0에서 시작합니다.

s1 = s[1]
print(s1)
s2to3 = s[1:3]
print(s2to3)
s4 = s[0:4]
#0번째부터 (4-1)번째까지
print(s4)
s7 = s[1:5:2]
#1번째부터 (5-1)번째까지 앞에서부터 글자 1개 제외
print(s7)
s77 = s[1:]
#끝 번호 생략 시 문자열의 끝까지 출력