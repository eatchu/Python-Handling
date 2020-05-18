'''
기본(default) 생성자
 - 생성자를 생략하면 기본 생성자가 만들어진다.
 - 묵시적 생성자
'''

class default_cost :
    # 생성자 생략
    '''
    def __init__(self): 기본 생성자
    '''
    def data(self,x,y):
        self.x = x
        self.y = y
    def mul(self):
        re = self.x * self.y
        return re

obj = default_cost() # 기본 생성자
obj.data(10,20) # 데이터 생성자의 역할을 대신함
obj.mul() # 200


# TV class 생성
class TV :
    # class 구성 =  변수(자료) + 메소드(함수)
    channel = volume = 0
    power = False # off(false) -> on(true)
    color = None
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
    def data(self,channel,volumn,color):
        self.channel = channel
        self.volume = volumn
        self.color = color
    # TV 정보 출력 메소드
    def display(self):
        print('전원 : {}, 채널 : {}, 볼륨 : {}, 색상 : {}'
              .format(self.power, self.channel, self.volume, self.color))

tv1 = TV()
tv1.display() # 객체의 초기 상태 = 전원 : False, 채널 : 0, 볼륨 : 0, 색상 : None

tv1.data(5,10,'검정색')
tv1.display() # 전원 : False, 채널 : 5, 볼륨 : 10, 색상 : 검정색

tv1.changepower() # off -> on
tv1.channelup() # 5 -> 6
tv1.volumeup() # 10 -> 11
tv1.display() # 전원 : True, 채널 : 6, 볼륨 : 11, 색상 : 검정색

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


