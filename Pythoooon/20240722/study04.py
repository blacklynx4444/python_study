'''
int : integer. 소수점이 없는 정수
float : 실수(소수점이 있는 수)
bool : boolean. 참(True)과 거짓(False) 2개의 값만 가집니다. 파이썬에서는 첫 글자를 대문자로 표기해야 합니다
str : string. ''나 ""로 감싸서 표현해야 하는 문자열 변수이며 흔히 말하는 텍스트입니다.
'''

'''
각각의 자료형은 형태를 변환할 수 있습니다.
print 시 문자열+문자열은 가능하지만 문자열+정수는 불가능하다. -> 문자열을 정수로 변환해야 한다.
'''

age = 26
print('나이 : ' + str(age)) #변수명 age를 문자열로 변환해야 오류 없이 출력된다.
print('')

light_on = True #boolean
print(light_on)
print(int(light_on))
print(float(light_on))
print('')
light_off = False #boolean
print(light_off)
print(int(light_off))
print(float(light_off))