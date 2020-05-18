'''
중첩함수(inner function)
형식)
def outer_funct(인수) :
    실행문
    def inner_func(인수) :
        실행문
    return inner_func
'''

# 1. 중첩함수 예
def a() : # outer
    print('a 함수')
    def b() : # inner
        print('b 함수')
    return b # inner func

b = a() # a 함수 출력
b() # b 함수 출력


# 2. 중첩함수 응용
'''
inner 함수 종류
 - getter(): 함수내에서 사용하는 data를 외부로 꺼내옴
   형식) 인수는 없고 함수내에 저장된 데이터를 return에 입력함 (변형된 내용을 외부에서 보기 위해 사용)
 - setter(): 함수내에서 사용하는 data를 수정 및 변경함
outer 함수 역할
 - 데이터 저장
 - inner 함수 포함
'''

def outer_func(data) :
    dataSet = data # 데이터 저장, inner 포함

    # 연산을 목적으로 하는 inner 함수
    def tot() : # inner :  저장된 데이터를 조작
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val) :
        avg_val = tot_val/len(dataSet)
        return avg_val

    # getter 함수
    def getData() :
        return dataSet

    # setter 함수
    def setData(newData) :
        nonlocal dataSet # outer 변수를 사용하겠다고 지정해주는 함수
        dataSet = newData # 지역변수

    return tot, avg, getData, setData



data = list(range(1,101))

tot, avg, getData, setData = outer_func(data)
tot_val = tot()
avg_val = avg(tot_val)

print('tot=',tot_val) # 5050
print('avg=',avg_val) # 50.5
print('dataset=', getData())


# 값 전부 변경
newData = list(range(1,51))
setData(newData) # 데이터 변경
print('dataset=', getData()) # 변경 확인
print('tot=',tot_val) # 1275
print('avg=',avg_val) # 25.5
print('dataset=', getData()) # [1~50]


# 3. 함수 장식자 : Tensorflow2.0에서 적용
# - 기존 함수의 시작부분과 종료부분에 기능을 추가해서 장식 역할
'''
@ 함수 장식자
def 함수명 ()
    실행문
'''

# 함수장식자 작성
def hello_doco(func) : # outer func
    def inner(name) : # 장식자 역할
        print('-'*20)
        func(name)
        print('-'*20)
    return inner

@ hello_doco
def hello(name):
    print('my name is %s'%(name))

hello('이순신')


'''
--------------------
my name is 홍길동!
--------------------
'''



'''
********2단********
2x1  = 2
 .
 .
2x9 = 18
'''


# 구구단
def gugu_deco(func) :
    def inner(dan) :
        print('******%d단*****'%(dan))
        func(dan)
        print('*************')
    return inner


@gugu_deco
def gugu(dan) :
    for i in range(1,10) :
        print('%d x %d = %d'%(dan,i,dan*i))

dan = int(input('구구단을 입력하시오 :'))
gugu(dan)

