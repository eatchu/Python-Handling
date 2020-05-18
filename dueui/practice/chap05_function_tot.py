
# ppt 내장함수 실습하기 ~ 4월 말

'''
step01 func_basic
'''

# 1. 사용자 정의함수
# 1) 인수가 있는것
# 2) 인수가 없는것
# 3) 리턴이 있는것

# 2. 라이브러리 함수
# 1) built - in : sum, max, min, len, abs
# 2) import :
import statistics
print(dir(statistics)) # 해당 모듈의 정보
'''
ctrl + 클릭 : module or function source 보기 
'''


'''
step02 사용자 정의 함수 응용
'''

# 텍스트 전처리 용도
def clean_txt(texts) :
    from re import findall, sub
    # 소문자 변경
    text1 = [text.lower() for text in texts]
    # 슷자 제거
    text2 = [sub('[0-9]','',text) for text in text1]
    # 문장부호 제거
    punc_str = '[.,;:?!]'
    text3 = [sub(punc_str,'',text)for text in text2]
    # 특수문자 제거
    func_str = '[~@#$%^&*()]'
    text4 = [sub(func_str,'',text) for text in text3]
    # 공백 제거
    text5 = [sub('\s{2,}',' ',text)for text in text4]
    return text5

texts = [' 우리나라    대한민국, 우리나라%$ 만세',
         '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람',
         '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
print(texts)
print(clean_txt(texts))

# 표본의 분산과 표준편차
# - 평균,분산,표준편차(from statistics) + 루트(from math) 함수 호출
from statistics import mean, variance, stdev
from math import sqrt
dataset = [2,4,5,6,1,8]

def var_std(dataset) :
    avg = mean(dataset)
    sum = 0
    for i in dataset :
        sum += (i-avg)**2
    var = sum/(len(dataset)-1)
    std = sqrt(var)
    return var, std

print(var_std(dataset))


'''
step03 가변인수
'''


# 패키지.모듈
'''
외부에서 작업한 사용자 정의함수를 가져와서 사용할 수 있다
'''
# import 패키지.모듈
# from scatter(패키지명).scatter_module(모듈명) import Avg, var_std (함수1,함수2)

'''
1. tuple형 가변인수 : 변수(a,*b)
2. dict형 가변인수 : 변수(a,**b)
* : 나머지 원소를 tuple 형태로 받는다
** : 나머지 원소를 dict 형태로 받는다
'''


'''
step04 lambda & scope
'''
# lambda 축약함수
add = lambda x,y,z : x + y + z
add(1,2,3) # 6

# scope
# 지역함수 vs 전역함수
x = 30
def try_1(x) :
    x = x*x
    return x

try_1(x) # 900
print(x) # 30

# global 함수 - 인수 사용 x
x = 30
def try_2() :
    global x
    x = x*x
    return x

try_2() # 900
print(x) # 900

'''
step05 inner function
'''

def Operate_func(data) :
    dataset = data
    def getvalue() :
        return dataset
    def Tot() :
        value = sum(dataset)
        return value
    def Avg(value) :
        avg = value/(len(dataset))
        return avg
    def setvalue(new) :
        nonlocal dataset
        dataset = new
    return getvalue, Tot, Avg, setvalue

data = list(range(1,101))
getData, tot, avg, setData = Operate_func(data)
getData() # 1 ~ 100
value = tot() # 5050
avg(value) # 50.5
setData(list(range(1,51))) # 데이터 값 변경
getData() # 1 ~ 50


# 함수 장식자
def create(func) :
    def create2(name):
        print('*' * 30)
        func(name)
        print('*' * 30)
    return create2

@create
def names(name) :
    print('제 이름은 %s입니다'%(name))

names('유관순')
'''
******************************
제 이름은 유관순입니다
******************************
'''

'''
step06 recursive 재귀함수
'''

# 누적재귀함수

def Adder(n) :
    if n == 1 :
        return 1
    else :
        result = n + Adder(n-1)
        '''
        1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1)] 1(2-1)
        2. stack 역순으로 값을 누적 : 1 + [2+3+4+5]
        '''
        print(result, end = ' ')
        return result

print(Adder(1)) # 1
print(Adder(5)) # 15


