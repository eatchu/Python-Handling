'''
반복문(while) : 조건이 참인 동안 반복을 계속함
               조건이 거짓이 되면 반복문이 멈춤
while 조건식 :
      실행문
      실행문
'''

# 카운터, 누적 변수
cnt = tot = 0
while cnt < 5 :
    cnt += 1 # 카운터 변수
    tot += cnt # 누적 변수
    print(cnt,tot)

# 1~100까지 합 출력
cnt = tot = 0
data = [] # 빈 list : 원소들을 1차원의 형태로 저장 가능
while cnt < 100 :
    cnt += 1 # 카운터 변수
    tot += cnt # 누적 변수
    if cnt % 2 == 0 :
        data.append(cnt) # 짝수의 값 저장

print(tot)
print('1~100까지의 합 : %s'%(tot))
print(data) # 백터 형태로 짝수값만 저장됨


# 문제) 1~100 사이에서 5의 배수이면서 3의 배수가 아닌 값만 append하기
data = []
cnt = 0
while cnt < 100 :
    cnt += 1
    if cnt % 5 == 0 and cnt % 3 != 0:
        data.append(cnt)
print(data)


# 무한 Loop -> 종료 조건(0)
while True :
    num = int(input('숫자입력 :'))
    if num == 0 :
        print('프로그램 종료')
        break # 탈출(exit) : 종료조건
    print('num=',num)



# random : 난수 생성
import random # 난수 생성 모듈
r = random.random() # 모듈.함수(0~1 난수)
print('r=',r)
help(random.random) # 0~1 사이의 난수 실수
help(random.choice) # ?
help(random.randint) # 난수 정수


# 문제) 난수 0.01 미만이면 종료, 아니면 난수 갯수 출력
cnt = 0
while True :
    r=random.random()
    cnt += 1
    if r < 0.01 :
        print('난수는 0.01 이상인 갯수', cnt,'개')
        break
    else :
        continue

r = random.randint(1,5) #(1,5) 범위 지정_
print(r)


print('숫자 맞추기 게임')
'''
myinput == computer : 성공(exit) -> 종료 조건
myinput > computer : '더 작은 수를 입력하라'
myinput < computer : '더 큰 수를 입력하라'
'''

computer = random.randint(1,10)
while True :
    myInput = int(input('숫자를 맞추시오 : '))
    if myInput == computer :
        print('성공! 답 =', computer)
        break
    else :
        if myInput > computer :
            print('더 작은 수를 입력하시오')
        else :
            print('더 큰 수를 입력하시오')

'''
- 반복문에서 사용되는 명령어
- continue : 반복을 지속, 다음 문장 skip
- break : 반복 멈춤
'''
i = 0
while i < 10 :
    i += 1
    if i==3 :
        continue
    if i==6 :
        break
    print(i,end=' ')



















