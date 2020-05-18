'''
정규 표현식

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''



# 모듈을 꺼내서 함수를 사용하는 두가지 방법
import re # 방법1) 정규표현식 모듈 꺼내기
re.findall() # 방법1 -> 사용
from re import findall, match, sub # 방법2) from 모듈 import 모듈에 속한 함수들
findall() # 방법2 -> 사용


# 1. findall
# 형식) findall(pattern='메타문자 패턴', string='문자열')

st1 = '1234 abc홍길동 ABC_555_6 이사도시'

# 1) 숫자 찾기
print(re.findall('1234', st1)) # ['1234']
print(findall('[0-9]{3}', st1)) # ['123','555']
print(findall('[0-9]{3,}', st1)) # ['1234','555']
print(findall('\d{3,}', st1)) # ['123','555']


# 2) 문자열 찾기
print(findall('[가-힣]{3,}',st1)) # ['홍길동', '이사도시']
print(findall('[a-z]{3}',st1)) # ['abc']
print(findall('[a-z|A-Z]{3}',st1)) # ['abc', 'ABC']


str_list = st1.split(sep=' ')
print(str_list) # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names = []
for s in str_list :
    tmp = findall('[가-힣]{3,}',s)
    print(tmp)
    if tmp : # [] -> False, ['값'] -> True
        names.append(tmp[0]) # 단일 list
        names.append(tmp) # 중첩 list
print(names)

# tmp[0]으로 사용하는 이유 : 리스트를 제거해 중첩리스트를 방지
d = ['두의']
d # ['두의']
d[0] # '두의'


# 3) 접두어/접미어 문자열 찾기

st2 = 'test1abcABC 123mbc 45test'

# 문장 전체의 처음과 끝의 문자열 출력
print(findall('^test',st2)) # ['test']
print(findall('^[a-z]{3,}',st2)) # ['test']
print(findall('[a-z]{3,}$',st2)) # ['test']

# 종료 문자 찾기
print(findall('.bc',st2)) # ['abc', 'mbc']
print(findall('.est',st2))

# 시작 문자 찾기
print(findall('t.',st2)) # ['te', 't1', 'te']


# 4) 단어 찾기(\\w) : 한글, 영문자, 숫자

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{2,}', st3)
print(words) # ['test', '홍길동', 'abc', '대한', '민국', '123', 'tbc']


# 5) 특정 문자열 제외
print(findall('[^t]+', st3)) # +를 사용하지 않으면 결과값이 음절로 끊어져서 나옴
print(findall('[^t]*', st3)) # 스페이스 포함
print(findall('[^t]?', st3)) # 음절로 출력

# 특수문자 제외
print(findall('[^^*$]+',st3))



# 2. match
# 형식) match(pattern='패턴', string='문자열')
# - 패턴 일치 여부 반환 (일치 : object반환, 불일치 : NULL 반환)

jumin = '123456-1234567'
jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4]\\d{6}', jumin)
print(result) # None이 나온다면 -> False
if result :
    print('정상 주민번호이다')
else :
    print('잘못된 주민번호이다')


# 3. sub
# 형식) sub('pattern 찾는패턴','rep 바꿀 값','string')
# - R의 gsub와 유사한 함수로 문자 전처리할때 사용

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

result = sub('[^*$]',' ',st3)
print(result) #   *    $  값이 이상하게 나옴


result = sub('[\^*$]',' ',st3) # 특수문자들 앞에 \ 삽입
print(result) # test 홍길동 abc 대한 민국 123 tbc 원하는 값 추출












