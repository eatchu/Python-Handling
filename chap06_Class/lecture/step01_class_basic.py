'''
클래스(class)
 - 함수의 모임
 - 역할 : 다수의 함수와 공유 자료를 묶어 객체를 생성
 - 유형 : 사용자 정의 클래스, 라이브러리 클래스(python)
 - 구성 요소 : 멤버 + 생성자
 - 멤버(member) : 변수(자료 저장) + 메소드(자료 처리)
 - 생성자 : 객체 생성
 형식)
 class 클래스명(괄호x) :
 멤버변수 = 자료
 멤버메소드() = 자료처리
 생성자 : 객체 생성
'''

# 1. 중첩함수
def calc_func(a,b) : # outer 함수 : inner 함수가 데이터를 처리할 수 있게 데이터를 저장해주는 역할
    # 자료 저장
    x = a
    y = b
    def plus() : # inner 함수 : 자료 처리 (조작)
        return x + y
    def minus() :
        return x - y
    return plus, minus

plus, minus =calc_func(10,20)
plus() # 30
minus() # -10


# 2. 클래스 정의
class calc_class : # class define
    # 멤버변수(x,y) : 자료 저장
    x = y = 0 # 클래스 내에서 사용할 자료들

    # 생성자 : 객체를 생성하거나 멤버변수의 값을 기본으로 초기화하는 역할
    def __init__(self,a,b): # self :  매개체 역할
        self.x = a
        self.y = b
    # 멤버 메소드 :  클래스에서 정의한 함수
    def plus(self):
       return self.x + self.y

    def minus(self):
        return self.x-self.y

# 생성자 -> 객체1(object)
obj1 = calc_class(10,20)
# object.member()
print('plus=', obj1.plus()) # 30
print('minus=', obj1.minus()) # -10
# object.member : 멤버변수 호출
print('x=',obj1.x) # 10
print('y=',obj1.y) # 20


# 생성자 -> 객체2
obj2 = calc_class(100,200)
obj2.plus() # 300
obj2.minus() # -100


# 객체 주소 확인
print(id(obj1), id(obj2)) # 2202718163400  2202718165512


# 3. 라이브러리 클래스 (이미 만들어진 클래스)
# 이미 만들어진 클래스 함수를 ctrl로 확인하여 생성자 형식을 확인하고
# 구하고자 하는 값을 넣어 객체를 쉽게 만들 수 있다
from datetime import date # from 모듈 import 클래스

today = date(2020,4,13) # 생성자 -> 객체 만들기

#object.member : 멤버 변수 호출
today.year # 2020
today.month # 4
today.day # 13

# object.member() : 멤버 메소드 호출
today.weekday() # 0 = 월요일
today.isoweekday()

