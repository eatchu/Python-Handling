'''
1. 축약함수(lambda)
 - 한 줄 함수
 - 리스트 내포를 쓸때 주로 사용
 형식) 변수 = lambda 인수 : 리턴값
 ex) lambda x,y : x+y

2. scope
 - 전역변수, 지역변수(함수 내)

'''

# 1. 축약함수
def adder(x,y) :
    add = x + y
    return add

add = lambda x,y : x + y
# [lambda x,y : x + y for 변수 in 열거형 객체]
add(10,20) # 30

add = lambda x,y,z : x + y + z
add(1,2,3) # 6


# 2. scope

x = 50 # 전역변수

def local_func(x) :
    x += 50 # 지역변수 x = 100
    print(x) # 100
    # 해당 함수가 종료되면 자동으로 소멸

local_func(x) # 100
print(x) # 50


def global_func() :
    global x # 전역변수 x를 쓰겠다는 의미
    x += 50
global_func()
print(x)


