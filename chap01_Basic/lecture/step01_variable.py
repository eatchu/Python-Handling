'''
변수(variable)
- 형식) 변수명 = 값 or 수식 or 변수명
- 자료를 저장하는 메모리 이름
- type 선언 없음 (R 동일)
'''

# 1. 변수와 자료
var1 = "Hello python"
var2 = 'Hello python' # '' 와 "" 둘다 사용 가능
print(var1) # line skip 자체 줄바꿈 기능
print(var2)
# 변수 자료형 확인
print(type(var1),type(var2)) # <class 'str'> 문자형

var1 = 100
print(var1, type(var1)) # 100 <class 'int'> 정수형

var3 = 150.25
print(var3, type(var3)) # 150.25 <class 'float'> 실수형

var4 = True
print(var4, type(var4)) # True <class 'bool'> 논리형

# 2. 변수명 작성규칙 (p.11참조)
_num10 = 10
_NUM10 = 20
# 대소문자 구분
print(_num10, _NUM10)
print(id(_num10), id(_NUM10)) # 140710480346464 140710480346784 값이 저장된 메모리 주소 = 다름


# 키워드 확인
import keyword # 모듈 임포트
py_keyword = keyword.kwlist # 키워드 반환
print('파이썬 키워드:', py_keyword)
print('len=', len(py_keyword)) #len= 35



# 낙타체
korScore = 90 # 변수 = 상수
matScore = 85
engScore = 75

tot = korScore + matScore + engScore
print('tot=',tot)

# 3. 참조변수 : 메모리 객채(value)를 참조하는 주소 저장 변수
x = 150 # 객체의 주소
x2 = 150 # 기존 객체가 있으면 객체를 만들지 않고 해당 객체의 주소를 반환한다
         # 즉 x의 주소를 가져와 x와 같은 메모리 주소를 가지게 됨 (메모리 효율적 사용)
y = 45.23
y2 = y # 변수 복제
# 변수 내용 출력
print(x, y, y2, x2)
# 변수 주소 출력
print(id(x), id(y), id(y2), id(x2))





