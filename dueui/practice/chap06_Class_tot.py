'''
step01 class
'''

# 클래스 정의
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

# 생성자 -> 객체(object)
obj = calc_class(10,20)
# object.member()
print('plus=', obj.plus()) # 30
print('minus=', obj.minus()) # -10
# object.member : 멤버변수 호출
print('x=',obj.x) # 10
print('y=',obj.y) # 20


# 라이브러리 클래스 (이미 만들어진 클래스)
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


'''
step 02 Car
'''

# 기본 변수가 아닌 새로운 변수 추가하기
class Car :

    # 생성자
    def __init__(self, door, cc, name=None):
        self.door = door
        self.cc = cc
        self.name = name
    # 멤버 메소드 : 자료 처리
    def info(self):
        self.kind = "" # 동적멤버 변수 (새로운 변수 생성)
        if self.cc >= 3000 :
            self.kind = "대형"
        else :
            self.kind = "소형"
        self.display()

    def display(self):
        print('%s는 %d cc이고(%s), 문짝은 %d개 이다.'
              %(self.name, self.cc, self.kind, self.door))

# 객체
car = Car(4,2000,'소나타')
print(car.name) # 소나타
car.info() # 소나타는 2000 cc이고(소형), 문짝은 4개 이다.

'''
step03 TV
'''

# TV class 생성
class TV :
    # class 구성 =  변수(자료) + 메소드(함수)
    channel = volume = 0
    power = False # off(false) -> on(true)
    def volumeup(self):
        self.volume += 1
    def volumedown(self):
        self.volume -= 1
    def channelup(self):
        self.channel += 1
    def channeldown(self):
        self.channel -= 1
    def changepower(self):
        self.power = not(self.power) # 반전 (T -> F)
    # TV 생성 메소드
    def data(self,channel,volumn):
        self.channel = channel
        self.volume = volumn
    # TV 정보 출력 메소드
    def display(self):
        print('전원 : {}, 채널 : {}, 볼륨 : {}'
              .format(self.power, self.channel, self.volume))
'''
문제) tv2 객체를 다음과 같이 생성하시오.
     단계1 : 전원 F 채널 1 볼륨 1 색상 파랑색
     단계2 : 전원 T 채널 10 볼륨 15
     단계3 : tv2 객체 정보 출력
'''
tv2 = TV()
tv2.data(1,1,'파랑색')
tv2.changepower()
# while or for
while tv2.channel < 10 :
    tv2.channelup()
for i in range(14) :
    tv2.volumeup()
tv2.display() # 전원 : True, 채널 : 10, 볼륨 : 15, 색상 : 파랑색


# 생성자 입력 vs 생성자 입력x
# 생성자 입력
class obj_class1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def tot(self):
        plus = self.x+self.y
        return plus
# 객체를 생성할때 값을 같이 입력함
obj1 = obj_class() # error
obj1 = obj_class1(10,20)
obj1.tot() # 30

# 생성자 입력x
class obj_class2:
    def tot(self,x,y):
        self.x=x
        self.y=y
        plus = self.x+self.y
        return plus
# 객체를 생성한 후 함수를 사용할때 값을 입력함
obj2 = obj_class2(10,20) # error
obj2 = obj_class2()
obj2.tot(10,20) # 30

'''
step04 Account
'''

class bank_account:
    balance = 0  # 잔액(balance)

    def data(self, balance):
        self.balance = balance

    def getBalance(self):  # 잔액확인(getter)
        print('현재 계좌 잔액은 {}원 입니다.'.format(self.balance))

    def deposit(self):  # 입금하기(setter)
        money = int(input('입금액을 입력하세요 : '))
        self.balance += money
        print('{}원 입금후 잔액은 {}원 입니다.'.format(money, self.balance))

    def withdraw(self):  # 출금하기(setter)
        money = int(input('출금액을 입력하세요 : '))
        if self.balance >= money:
            self.balance -= money
            print('{}원 출금후 잔액은 {}원 입니다.'.format(money, self.balance))
        else:
            print('잔액이 부족합니다')


count = bank_account() # 객체 생성
count.data(30000) # 잔액 입력
count.getBalance() # 현재 계좌 잔액은 15000원 입니다.
count.deposit() # 20000 -> 20000원 입금후 잔액은 35000원 입니다.
count.withdraw()
# 50000 -> 잔액이 부족합니다
# 30000 -> 30000원 출금후 잔액은 5000원 입니다.
count.getBalance() # 현재 계좌 잔액은 5000원 입니다.

'''
step05 Inheritance 상속
'''

# 부모클래스 정의
class Parent :
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def display(self):
        print('이름 : {}, 직업 : {}'.format(self.name, self.job))

parent = Parent('홍길동','공무원')
parent.display() # 이름 : 홍길동, 직업 : 공무원

# 자식 클래스 정의
class Childen1(Parent) :
    gender = None
    def __init__(self,name, job, gender):
        # Parent.__init__(self,name,job)
        super().__init__(name, job)
        self.gender = gender
    def display(self):
        print('이름 : {}, 직업 : {}, 성별 : {}'
              .format(self.name, self.job, self.gender))

# 자식 객체 생성
c1 = Childen1('이순신','군인','남자')
c1.display()

c2 = Childen1('유관순','독립열사','여자')
c2.display()

'''
step06 Override
'''
#  메소드 재정의 (method override)
# 부모클래스 생성
class Super :
    # 기본 생성자 : 객체만 생성
    # 멤버 메소드 : 원형 메소드
    def superFunc(self): # 인수x 내용x
        pass

# 자식클래스 생성 1
class Sub1(Super) :
    # 상속된 멤버
    # 1 data
    # 2 def superFunc
    def superFunc(self, data): # 수정 -> override
        self.data = data
        print('자식1 : data = {}'.format(self.data))

sub1 = Sub1()
sub1.superFunc('20200414') # 자식1 : data = 20200414

# 자식클래스 생성 2
class Sub2(Super) :
    def superFunc(self, data): # 수정 -> override
        self.data = data
        print('자식2 : data = {}'.format(self.data**2))

sub2 = Sub2()
sub2.superFunc(100) # 자식2 : data = 10000

# 다형성
sup = Super() # 부모 객체
sub1 = Sub1() # 자식1 객체
sub2 = Sub2() # 자식2 객체

sup = sub1 # 부모의 객체에 자식1 객체 입력
sup.superFunc(1234) # 부모객체에 멤버메소드를 호출하면 자식1 객체가 가지고 있는 멤버메소드 값이 나옴
# 자식1 : data = 1234
sup = sub2
sup.superFunc(1234)
# 자식2 : data = 1522756 (제곱값)


'''
step07 Inclusion
'''
# private 변수 (은닉변수)
class Login : # uid, pwd , name
    # 생성자
    def __init__(self, uid, pwd, name):
        # self.__private : 은닉변수
        self.__dbId = uid
        self.__dbPwd = pwd
        self.name = name

    # getter() : 획득자
    def getIdPwd(self):
        return self.__dbId, self.__dbPwd,self.name

log = Login('gh4582',88263662,'dueui')
log.getIdPwd()

class login_chk :
    def __init__(self,data):
        self.data = data
    def check(self, uid, pwd):
        Id,pd,name = self.data.getIdPwd()
        if Id == uid and pd == pwd :
            print(f'{name}님 로그인 하셨습니다')
        else :
            print('로그인에 실패하셨습니다')

server = login_chk(log)
server.check('gh4582',88263662) # dueui님 로그인 하셨습니다
server.check('gh4582',35813662) # 로그인에 실패하셨습니다


'''
step08 Module
'''
# 다른 위치에 존재하는 패키지의 모듈과 함수 꺼내오는 법

'''
step 09 package
'''
# 1. import fibo : 피보나치 수열을 구하는 패키지와 함수(fib)
# 2. import copy : 변수를 복사하는 패키지와 함수(deepcopy)
# 3. import keyword : iskeyword
# 4. import random -> random으로 숫자 여러개 출력하는 방법 찾기
import random # randint, random, choice
print(random.randint(1,100)) # 1~100 중에 랜덤으로 숫자 하나 출력
print(random.random()*100)
a = list(range(1,101)) # 변수에 1~100까지 숫자 입력
random.choice(a) # 변수안에 랜덤으로 하나를 출력
random.shuffle(a);print(a) # 순서를 랜덤하게 배열
# 5. import time -> 좀 더 연구
# 6. import calendar
import calendar
cal = calendar.month(2016,9)
print(cal) # 해당하는 달의 달력 출력


# 피보나치 수열 : 함수 사용
def fib(n):
    a,b=0,1
    while b<n:
        print(b,end=',')
        a,b = b, a+b
    print()
a = fib(1000)
# 피보나치 수열 : 패키지 사용
# import fibo or from fibo import fib
# fibo.fib(1000) or fib(1000)


# 성적 입력 후 리스트 저장
class Score:
    def __init__(self,data):
        self.nlist = data

    # 성적 입력 후 리스트 저장
    def readList(self):
        flag = True
        while flag:
            number = int(input('숫자를 입력하시오:'))
            if number < 0:
                flag = False
            else:
                self.nlist.append(number)
        return self.nlist

    # 성적순 정렬
    def processList(self):
        return self.nlist.sort()

    # 성적 출력
    def printList(self):
        for i in self.nlist:
            print('성적=', i)

a = []
b = Score(a)
b.readList()
b.processList()
b.printList()

