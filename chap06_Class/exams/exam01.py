'''
step01_Class01 관련 문제 
 문1) Rectangle 클래스를 작성하시오.
 <처리조건>
1. 멤버변수 : 가로(width), 세로(height) 
2. 생성자 : 가로(width), 세로(height) 멤버 변수 초기화  
3. 멤버함수(area_calc) : 사각형의 넓이를 구하는 메서드 
          사각형 넓이 = 가로 * 세로 
4. 멤버함수(circum_calc) : 사각형의 둘레를 구하는 메서드
          사각형 둘레 = (가로 + 세로) * 2
  5. 기타 나머지는 출력 예시 참조         
   
       << 출력 예시 >>       
    사각형의 넓이와 둘레를 계산합니다.
    사각형의 가로 입력 : 10
    사각형의 세로 입력 : 5
    ----------------------------------------
    사각형의 넓이 : 50
    사각형의 둘레 : 30
    ----------------------------------------
'''
print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))

class Rectangle :
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area_calc(self):
        return self.width * self.height
    def circum_calc(self):
        return (self.width+self.height)*2

###### 방법 1 ##########
def design(func) :
    def inner(w,h) :
        print('-'*20)
        func(w,h)
        print('-'*20)
    return inner

@ design
def hello(w,h):
    rect = Rectangle(w,h)
    print('사각형의 넓이 : %d'%(rect.area_calc()))
    print('사각형의 둘레 : %d'%(rect.circum_calc()))

hello(int(input('사각형의 가로 입력 : ')),int(input('사각형의 세로 입력 : ')))


####### 방법2 ##########

rect2 = Rectangle(int(input('사각형의 가로 입력 : ')),int(input('사각형의 세로 입력 : ')))
print('-'*20,'\n',
      '사각형의 넓이 : ',rect2.area_calc(),'\n',
      '사각형의 둘레 : ',rect2.circum_calc(),'\n',
      '-'*20)




