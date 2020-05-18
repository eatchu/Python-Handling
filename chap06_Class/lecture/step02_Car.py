'''
동적 멤버 변수 생성
 - 필요한 경우 특정 함수에서 멤버변수를 생성
 self : 클래스의 멤버를 호출하는 역할
 self.멤버변수
 self.멤버메소드
'''

class Car :
    # 멤버 변수
    # door = cc = 0  숫자 값이 들어갈 경우
    # name = None  문자 값이 들어갈 경우

    # 생성자
    def __init__(self, door, cc, name=None):
        # self.멤버변수 = 매개변수
        self.door = door
        self.cc = cc
        self.name = name
    # 멤버 메소드 : 자료 처리
    def info(self):
        self.kind = "" # 동적멤버 변수
        if self.cc >= 3000 :
            self.kind = "대형"
        else :
            self.kind = "소형"
        self.display()

    def display(self):
        print('%s는 %d cc이고(%s), 문짝은 %d개 이다.'
              %(self.name, self.cc, self.kind, self.door))

# 객체 1
car1 = Car(4,2000,'소나타')
print(car1.name) # 소나타
car1.info() # 소나타는 2000 cc이고(소형), 문짝은 4개 이다.

# 객체 2
car2 = Car(4,3000,'그랜저')
print(car2.name) # 그랜저
car2.info() # 그랜저는 3000 cc이고(대형), 문짝은 4개 이다.
