'''
클래스 상속(Inheritance)
 - 기존 클래스(부모)를 이용하여 새로운 클래스(자식) 생성 문법
 - 부모클래스 정의 -> 자식클래스 생성
 - 상속 대상 : 멤버(o) + 생성자(x)
   -> 생성자는 상속대상이 아님
 형식)
 class 자식클래스(부모클래스) : # class child(parent) :
       멤버(변수 + 메소드)
       생성자

self vs super()
 - self.member : 현재 클래스의 멤버변수를 호출
 - super().member : 부모 클래스의 멤버변수를 호출

'''

# 부모클래스
class Super :
    name = None
    age = 0
    # 생성자 : 객체 생성
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 멤버 메소드 : 데이터 처리
    def display(self):
        print('이름 : {}, 나이 : {}'.format(self.name, self.age))

# object 생성
sup = Super('부모',55)
sup.display() # 이름 : 부모, 나이 : 55
del super

# 자식 클래스
class Sub(Super) :
    # name = None # 부모 멤버 변수
    # age = 0 # 부모 멤버 변수
    gender = None # 자식 멤버 변수

    def __init__(self,name, age, gender): # 자식 생성자
        # 부모 생성자 호출
        #Super.__init__(self,name,age)
        super().__init__(name,age)
        self.gender = gender
        #self.name = name
        #self.age = age

    def display(self): # 2개 -> 3개
        print('이름 : {}, 나이 : {}, 성별 : {}'
              .format(self.name, self.age, self.gender))


sub2 = Sub('자식', 22, '남자')
sub2.display() # 이름 : 자식, 나이 : 22, 성별 : 남자


# 1. 부모클래스 정의
class Parent :
    name = job = None
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
        Parent.__init__(self,name,job)
        self.gender = gender
    def display(self):
        print('이름 : {}, 직업 : {}, 성별 : {}'
              .format(self.name, self.job, self.gender))

c1 = Childen1('이순신','군인','남자')
c1.display()


class Childen2(Parent) :
    def __init__(self, name, job, gender):
        Parent.__init__(self,name,job)
        self.gender = gender
    def display(self):
        print('이름 : {}, 직업 : {}, 성별 : {}'
              .format(self.name, self.job, self.gender))
c2 = Childen2('유관순','독립열사','여자')
c2.display()
