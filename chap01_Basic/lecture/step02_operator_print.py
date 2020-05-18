'''
연산자 (operator)
1. 변수에 값 할당(=)
2. 연산자 : 산술, 관계, 논리
3. print 형식
4. input 키보드 입력
'''

# 1. 변수에 값 할당(=)
i = tot = 10
i += 1 # i = i + 1 : 카운터 변수
tot += i # tot = tot + i : 누적 변수
print('i=', i) # i = 11
print('tot=', tot) # tot = 21

v1, v2 = 100 , 200 # v1=100 v2=200
print('v1=',v1,'v2=',v2)

# 변수 값 교체
v1,v2=v2,v1 # 값 바꾸기
'''
temp=v1
v1=v2
v2=temp
'''
print('v1=',v1,'v2=',v2)

# 패킹(packing) 할당
lst = [1,2,3,4,5] # vector : 1차원
v1, *v2 = lst
print('v1=',v1,'v2=',v2) # v1= 1 v2= [2, 3, 4, 5]

*v1, v2 = lst
print('v1=',v1,'v2=',v2)  # v1= [1, 2, 3, 4] v2= 5

'''
* : packing을 시킨다는 의미의 연산자
1. 리스트의 첫번째 원소는 v1, 나머지 원소는 v2로 들어감
2. 리스트의 처음 4개 원소는 v2, 나머지 한개 원소는 v2로 들어감
'''

# practice
dueui = [0,45,8,1]
*x,y = dueui
print(x)




# 2. 연산자 :  산술, 관계, 논리

# 1) 산술연산자
num1 = 100 # 피연산자1
num2 = 20.5 # 피연산자2
add = num1 + num2
dif = num1 - num2
mul = num1 * num2
div = num1 / num2 # 실수 몫
div2 = num1 //num2 # 정수 몫
div3 = num1 % num2 # 나머지
square = num1 ** 2 # 제곱
print(add,dif,mul)
print(div,div2,div3)
print(square)

# 2) 관계연산자 :  True or False
# 실습 ) num1 = 100, num2 = 20.5

# (1) 동등비교 : ==, !=
bool_re = num1 == num2
print(bool_re) # False

bool_re = num1 != num2
print(bool_re) # True

# (2) 대소관계 : >, >=, <, <=
bool_re = num1 >= num2
print(bool_re) # True

bool_re = num1 <= num2
print(bool_re) # False

# 3) 논리 연산자 : or, and, not
bool_re = num1 >= num2 or num1 <= 10
print(bool_re) # True

bool_re = num1 >= num2 and num1 <= 10
print(bool_re) # False

bool_re = not(num1 <= 10)
print(bool_re) # True

num1, num2 = 100, 20.5
bool(num1 >= num2 and num1 <= 10)

# 3. print 형식
help(print) # 함수 도움말
# package > module > function or class
# Help on built-in function print in module builtins:
# print(value, ..., sep=' ', end='\n' : 기본속성 각 값마다 뛰어쓰기 적용 함수가 끝나면 자동 줄바꿈
# module builtins : 기본 모듈(python 설치 시 자동으로 설치되는 모듈)

'''
함수의 인수
매개변수 : 값을 넘겨 받는 변수
파라미터 : 값을 갖는 변수
%d 10진수 정수
%o 8진수 정수
%x 16진수 정의
%f 실수(%f전체자릿수.소수점자릿)
%s 문자열
%c 단일 문자열

'''

# 1) 기본 인수
print('values=',10+20+30)
print('출력1',end=',') # end의 기본속성을 바꿈 : 줄바꿈 -> ,
print('출력2') # 출력1,출력2 -> 값이 한줄에 같이 나옴
print('010','1111','2222',sep='-') # 010-1111-2222 -> sep : 구분자를 결정해줌

# 2) format (value, '형식')
print("원주율=", format(3.14159, "8.3f")) # 원주율=    3.142
print("금액 =", format(10000, "10d")) # 금액 =      10000
print("금액 =", format(125000, "3,d")) # 금액 = 125,000
print("금액 =", format(125000000, "3,d")) # 금액 = 125,000,000

# 3) print ("양식문자" %(값)) 21page 참고
# 형식) %(값)에 입력 되는 값들이 양식문자 조건에 맞게 입력되어 문장을 형성
num1 = 10; num2 = 20
tot = num1 + num2
print("%d + %d = %d" %(num1, num2, tot)) # 10 + 20 = 30
print("8진수 = %o, 16진수 = %x" %(num1,num1)) # 8진수 = 12, 16진수 = a
print('%s = %8.3f' %("PI", 3.14159)) # PI =    3.142

# 4) 외부 상수 받기
# "{}, {}" .format(value1, value2)
print("name : {}, age : {}".format("홍길동", 35)) # name : 홍길동, age : 35
print("name : {1}, age : {0}".format(35, "홍길동")) # 0 1 2 ... 순서대로 값 입력됨

# format 축약형 : sql
# 형식) f"문장{}"
# select * from emp where name = '홍길동'
name = '홍길동'
age = 35
sql = f"select * from emp where name = {name} and age = {age}"
print(sql)


# 4. input ("prompt") : 키보드 사용자 직접 입력
# 특징) 무슨 값이 들어와도 문자로 인식함
a = input("첫번째 숫자 입력 :")
b = input("두번째 숫자 입력 :")
print('a+b=', a + b) # a+b= 1020
# 숫자를 인식시키기 위해 int type을 입력해줌
a = int(input("첫번째 숫자 입력 :"))
b = int(input("두번째 숫자 입력 :"))
print('a+b=', a + b) # a+b= 30

'''
int(value) : value -> integer
float(value) : value -> float
str(value) : value -> string
'''

# str -> float
a = float(input("첫번째 숫자 입력 :"))
b = float(input("두번째 숫자 입력 :"))
print("a+b=", a+b)
print('b=', b)
print(type(b))

# str -> bool
print(int(False)) # 0
print(int(True)) # 1

# int -> bool
print(bool(-1245)) # True
print(bool(0)) # False


