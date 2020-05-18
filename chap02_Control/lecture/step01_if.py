'''
제어문 : 조건문(if), 반복문(while, for)
Python 블럭 : 콜론과 들여쓰기

형식1)
if 조건식 :
   실행문
   실행문
'''

var = 10
if var >= 10 :
    print('var =', var)
    print('var는 10보다 크거나 같다.')

print('항상 실행되는 영역')

'''
형식2)
if 조건식 :
   실행문1
else :
   실행문2
'''
var = 2
if var >= 5 :
    print('var는 5보다 크거나 같다')
else :
    print('var는 5보다 작다')


# 문1) 키보드 점수 입력 -> 60점 이상 : 합격, 미만 : 불합격
score = int(input('점수를 입력하세요 :'))
if score >= 60 :
    print('합격')
else :
    print('불합격')


# 현재 시간 반환
import datetime # module 임포트
today = datetime.datetime.now() # module.class.method()
print(today) # 2020-04-07 11:10:23.061312
# 요일 반환
'''
0~4 : 평일 (월,화,수,목,금)
5~6 : 주말
'''
week = today.weekday()
print(week) # 1 화요일

if week >= 5 :
    print('오늘은 휴일')
else :
    print('오늘은 평일') # 오늘은 평일


'''
형식3)
if 조건식1 :
   실행문
elif 조건식2 :
     실행문
else :
     실행문

# R에서는 elseif로 사용 -> Python은 elif
'''

# 문2) 키보드 score 입력 : A(100~90), B(89~80), C, D, F(59미만)
score = int(input('점수를 입력하세요 :' ))
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
print('당신의 점수는 %d이고, 등급은 %s이다.'%(score,grade))



# 블럭 if vs 라인 if
# 블럭 if
num = 9
if num >= 5 :
    result = num*2
else :
    result = num+2

print(result)

# 라인 if
# 형식) 변수 = 참실행문 if 조건문 else 거짓실행문
result = num * 2 if num >= 5 else num + 2
print(result)





























