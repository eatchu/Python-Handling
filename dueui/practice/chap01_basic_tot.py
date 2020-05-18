
'''
%d 10진수 정수
%o 8진수 정수
%x 16진수 정의
%f 실수(%f전체자릿수.소수점자릿)
%s 문자열
%c 단일 문자열
'''


'''
step01_variable
'''

# 참조변수
'''
각각 다른 변수에 같은 값을 넣을 경우
실제로는 새로운 변수가 생성된것이 아니라 
값을 가지고 있는 변수의 주소를 가져와 또다른 변수에
같은 메모리 주소를 넣는다 (메모리 사용을 효율적으로 함)
'''
x = 150
x2 = 150
print(id(x)==id(x2)) # True




'''
step02_operator
'''

# 변수 알고리즘
i += 1 # i = i + 1 : 카운터 변수
tot += i # tot = tot + i : 누적 변수
v1, v2 = 100 , 200 # 변수 두개 한번에 생성
v1, v2 = v2, v1  # 변수 값 교체


# 패킹(packing) 할당
lst = [1,2,3,4,5] # vector : 1차원
v1, *v2 = lst # 두개 패킹
*v3, = lst # 단일 패킹
v1, v2, *v3 = lst # 다수 패킹
'''
* : packing을 시킨다는 의미의 연산자
1. 리스트의 첫번째 원소는 v1, 나머지 원소는 v2로 들어감
2. 리스트의 처음 4개 원소는 v2, 나머지 한개 원소는 v2로 들어감
'''


# boolean
num1, num2 = 100, 20.5
bool(num1 >= num2 and num1 <= 10) # False
bool(num1>num2) # True

# boolean 값 숫자로 정의하기
# str -> bool
print(int(False)) # 0
print(int(True)) # 1
# int -> bool
print(bool(-137)) # 값이 있으면 True
print(bool(0)) # 0이면 무조건 False




# format 및 값을 나타내는 여러가지 형식
# 1) format(value, '형식')
print(format(3.5714,'2.3f')) # 소숫점 3자리까지만 출력
# 2) ("양식문자" %(값))
print('내 이름은 %s이고 나이는 %d살이야'%('두의',26))
# 내 이름은 두의이고 나이는 26살이야
print('%s = %.3f' %("PI", 3.14159))
# PI =3.142
# 3) "{}, {}" .format(value1, value2)
# - 순서 지정 가능
print('내 이름은 {1}이고 나이는 {0}살이야'.format(26,'두의'))
# 4) f"문장{}"
name = '두의'
age = 26
print(f'내 이름은 {name}이고 나이는 {age}살이야')



'''
step03_string
'''

'''
count, find, index, rfind, startswith, split, join, swapcase
'''

# 문자열 처리 함수
lineStr = 'this is One Ling String'
len(lineStr) # 23 : 문자열 길이
lineStr.count('t') # 2 : 문자열에서 t가 몇개있는지 갯수 반환
lineStr.find('t') # 0 : t가 제일 처음 나온 위치
lineStr.find('z') # -1 : 안나온 문자가 입력되면 -1로 반환
lineStr.index('t') # 0 : .find 함수와 동일하지만 문자열에 없는 문자가 입력되면 error가 뜨는게 차이점
lineStr.rfind('t')  # 18 : 제일 마지막에 나온 t의 위치
lineStr.startswith('this') # True : 문자열이 this로 시작했는지 논리값 반환
lineStr.startswith('that') # False
lineStr.split(' ') # ['this', 'is', 'one', 'ling', 'string'] : 공백을 기준으로 분리
' '.join(lineStr.split(' ')) # 'this is one ling string' : 공백을 기준으로 다시 합치기
lineStr.swapcase() # 'THIS IS oNE lING sTRING' : 대문자 -> 소문자, 소문자 -> 대문자


# escape 문자 처리
'''
escape 문자 : 명령어 이외 특수문자(',",\n,\t,\b)
'''
print('\nescape문자') # 줄바꿈 이후 escape문자
print('\\nescape문자') # \nescape문자 : \
print(r'\nescape문자') # \nescape문자 : r

# c:\python\work\test
print('c:\python\work\test') # c:\python\work	est
print('c:\\python\\work\\test') # c:\python\work\test
print(r'c:\python\work\test') # c:\python\work\test

# \t , \b
print('두의가\t밥을먹었다') # 두의가	밥을먹었다
print('두의가\b밥을먹었다') # 두의밥을먹었다






