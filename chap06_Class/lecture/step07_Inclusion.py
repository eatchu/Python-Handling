'''
1. private 변수 = 클래스 내의 은닉변수
   object.member : 객체 -> 은닉변수(x)
   getter()/setter() -> 은닉변수(o)
2. class 포함관계(inclusion)
 - 특정 객체 다른 객체를 포함하는 클래스 설계 기법
 - 두 객체 간의 통신 지원
 - ex) class A(a) -> class B(b)
'''

# 1. private 변수
class Login : # uid, pwd -> db 저장
    # 생성자
    def __init__(self, uid, pwd):
        # self.__private : 은닉변수
        self.__dbId = uid
        self.__dbPwd = pwd

    # getter() : 획득자
    def getIdPwd(self):
        return self.__dbId, self.__dbPwd

    # setter() : 지정자(인수)
    def setIdPwd(self, uid, pwd):
        self.__dbPwd = pwd
        self.__dbId = uid


# object
login = Login('hong','1234')
#login.__dbID # error

# object.getter()
uid,pwd = login.getIdPwd()
print(uid,pwd,sep=',') # hong,1234

# object.setter()
login.setIdPwd('lee','2345')
uid,pwd = login.getIdPwd()
print(uid,pwd,sep=',') # lee,2345



# Server <-> Login
class Server :
    # 기본 생성자

    # 멤버 메소드
    def send(self, obj): # object 인수로 받음
        self.obj = obj # 멤버변수 생성

    # 인증 메소드
    def cert(self, uid, pwd): # 사용자(id/pwd)
        dbId,dbPwd = self.obj.getIdPwd() # getter 호출
        if dbId == uid and dbPwd == pwd :
            print('로그인 성공')
        else :
            print('로그인 실패')
server = Server()
server.send(login)
server.cert('hong','1234') # 로그인 실패
server.cert('lee','2345') # 로그인 성공

