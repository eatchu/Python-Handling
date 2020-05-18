# 정보 은닉
class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

obj = Student()
print(obj.__age) # 변수를 암호화해서 값이 안나옴


# getter, setter
class Student:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def setName(self, name):
        self.name = name

obj = Student("Hong", 20)
obj.getName()
obj.getAge()
obj.setAge(26)
obj.getAge()
obj.age
obj.name
# 왜 멤버 변수가 안나오지?


# 사각형을 클래스로 정의한다.
class Rectangle:
    def __init__(self, side=0):
        self.side = side
    def getArea(self):
        return self.side * self.side


# 사각형 객체와 반복횟수를 받아서 변을 증가시키면서 면적을 출력한다.
def printAreas(r, n):
    while n >= 1:
        print(r.side, "\t", r.getArea())
        r.side = r.side + 1
        n = n - 1


rect = Rectangle()
count = 5
rect.side # 0
printAreas(rect,count)
rect.side
rect.getArea()