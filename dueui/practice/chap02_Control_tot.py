'''
step 01 if
'''

# 현재 시간 반환 및 요일 구하기
import datetime
today = datetime.datetime.now() # module.class.method()
print(today) # 2020-04-07 11:10:23.061312
# 요일 반환
'''
0~4 : 평일 (월,화,수,목,금)
5~6 : 주말
'''
week = today.weekday()
print(week) # 1 화요일


# 라인 if
# 형식) 변수 = 참실행문 if 조건문 else 거짓실행문
num = 9
result = num * 2 if num >= 5 else num + 2 # 참
print(result) # 9 * 2 = 18



'''
step 02 while
- 조건이 참이 되는 동안 반복문 실행
- 무한 반복 루프도 생성 가능
'''

# random : 난수 생성
import random # 난수 생성 모듈
print('r=',r)
help(random.random) # 0~1 사이의 난수 실수
help(random.choice) # 여러 값중에 임의의 값 하나만 반환
help(random.randint) # 난수 정수




'''
step 03 for
열거형객체(iterable) 사용 가능 : string, list, tuple, set/dict
'''

# 1. string이 열거형 객체로 사용될 경우
# 한 음절음절 출력 됨
# ex) '안녕하세요.' -> 안 녕 하 세 요 .

# 2. list가 열거형 객체로 사용될 경우
# 한 인덱스마다 출력 됨
# ex) ['안녕','잘가','잘자'] -> 안녕 잘가 잘자

# 1~100 원소를 갖는 list 객체 생성 - range 사용
# for문에 열거형 객체로 사용할때 많이 쓰임
list(range(1,101)) # 1~100


# True/False 값 활용하기
for i in range(size) :
    fit = int(y[i]==y_pred[i]) #int(True/False) => 1/0
    acc += fit * 20
print('분류정확도 =',acc)


# 숫자 맞추기 게임
import random
# 실제 값 생성 - 랜덤으로 저장됨
real = []
for i in range(5) :
    real.append(random.choice([1,2,3,4,5]))
# 임의 값 입력
pred = []
for i in range(5) :
    pred.append(int(input('값을 입력하시오 :')))
# 분류 정확도 만들기
acc = 0
num = 0
for i in range(5) :
    num += 1
    if real[i] == pred[i] :
        fit = int(real[i] == pred[i])
        acc += fit
print(acc/num*100,'%')
print(pred,real)