'''
1. 메소드 재정의 (method override)
 - 부모의 원형 메소드 -> 자신의 원형 메소드를 다시 작성하는 문법
 - 상속관계에서만 나오는 용어
 - 인수, 내용 -> 수정 대상
2. 다형성
 - 상속관계에서만 나오는 용어
 - 한 가지 기능 -> 2개 이상 결과 생성(+ -> 덧셈, 결합)
 - 부모 객체 -> (자식1, 자식2...) 멤버 호출
'''

# 1. 메소드 재정의 (method override)
# 부모클래스 생성
class Super :
    data = None # 멤버 변수

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
    # 1 data
    # 2 def superFunc

    def superFunc(self, data): # 수정 -> override
        self.data = data
        print('자식2 : data = {}'.format(self.data**2))

sub2 = Sub2()
sub2.superFunc(100) # 자식2 : data = 10000


# 2. 다형성
sup = Super() # 부모 객체
sub1 = Sub1() # 자식1 객체
sub2 = Sub2() # 자식2 객체

sup = sub1 # 부모의 객체에 자식1 객체 입력
sup.superFunc(1234) # 부모객체에 멤버메소드를 호출하면 자식1 객체가 가지고 있는 멤버메소드 값이 나옴
# 자식1 : data = 1234
sup = sub2
sup.superFunc(1234)
# 자식2 : data = 1522756 (제곱값)





