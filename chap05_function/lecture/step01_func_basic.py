'''
함수(Function)
 - 중복 코드 제거
 - 재사용 가능
 - 특정 기능 1개 정의
 - 유형) 사용자 정의 함수, 라이브러리 함수
'''

# 1. 사용자 정의 함수
'''
형식)
def 함수명(매개변수) :
    실행문
    실행문
    return 값1, 값2 ...
'''

# 1) 인수가 없는 함수
def userFunc1() : # 함수 정의
    print('인수가 없는 함수')
    print('userFunc1')
userFunc1() # 함수 호출
# 인수가 없는 함수
# userFunc1

# 2) 인수가 있는 함수
def userFunc2(x,y) :
    adder = x+y
    print('adder=',adder)
userFunc2(10,20) # adder = 30

# 3) 리턴이 있는 함수
def userFunc3(x,y) :
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add, sub, mul, div # 외부에 값을 지정
a,s,m,d = userFunc3(100,20)
print(a,s,m,d)



# 2. 라이브러리 함수
'''
1) built-in : 기본함수
2) import : 모듈.함수()
'''

# 1) built-in
# sum, max, min, len
dataset = list(range(1,6))
print(dataset)
print('sum=',sum(dataset))

# 2) import
import statistics # 통계 관련 함수 제공
# statics 통계관련 함수 : 평균, 중위수, 최빈수 등
'''
ctrl + 클릭 : module or function source 보기 
'''

from statistics import mean # 방법2)

print(dir(statistics)) # 해당 모듈의 정보

avg1 = statistics.mean(dataset)
avg2 = mean(dataset)  #//얘를 더 많이 쓴다. -> 모듈.함수명 이렇게 보다 더 편하고 메모리 효율적이다

print('평균(avg1)=',avg1,'평균(avg2)=',avg2)




