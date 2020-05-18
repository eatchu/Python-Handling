'''
step01 RegEx
 - list 형태로 반환 됨
'''

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

'''
정규 표현식 2

\\ : 역슬래쉬 문자 자체
\d = [0-9] : 모든 숫자 <-> \D : 숫자가 아닌것
\w = [a-zA-Z0-9] : 숫자 또는 문자 <-> \W : 숫자나 문자가 아닌것
\s = [\t\n\t\f\v] : 화이트 스페이스 <-> \S : 스페이스가 아닌것
\b : 단어의 경계(영문자 혹은 숫자) <-> \B : 단어의 경계가 아닌것
\A : 문자열의 처음 <-> \Z : 문자열의 끝
'''


'''
주요 메소드
compile, match, search, split, findall, finditer
sub, subn, escape
'''

from re import compile, match, search, split, findall, finditer, sub, subn, escape


# findall
st1 = '1234 abc홍길동 ABC_555_6 이사도시'

str_list = st1.split(sep=' ')
# ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names = []
for s in str_list :
    tmp = findall('[가-힣]{3,}',s)
    print(tmp)
    if tmp : # [] -> False, ['값'] -> True
        names.append(tmp[0]) # 단일 list

print(names) # ['홍길동', '이사도시']


# 접두어/접미어
st2 = 'test1abcABC 123mbc 45test'

print(findall('^[a-z]{3,}',st2)) # ['test']
print(findall('[a-z]{3,}$',st2)) # ['test']
print(findall('.bc',st2)) # ['abc', 'mbc']
print(findall('t.',st2)) # ['te', 't1', 'te']


# 특정 문자열 제외
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(findall('[^t]+', st3)) # +를 사용하지 않으면 결과값이 음절로 끊어져서 나옴
print(findall('[^t]*', st3)) # 스페이스 포함
print(findall('[^t]?', st3)) # 음절로 출력
print(escape(st3)) # test\^홍길동\ abc\ 대한\*민국\ 123\$tbc



# match
jumin = '123456-1234567' # 정상 주민번호
jumin = '123456-5234567' # 잘못된 주민번호
result = match('[0-9]{6}-[1-4]\\d{6}', jumin)
print(result) # None이 나온다면 -> False
if result :
    print('정상 주민번호이다')
else :
    print('잘못된 주민번호이다')



'''
step02 텍스트 전처리 
'''

def clean_text2(texts) :
    from re import sub
    # 1. 소문자 변경
    texts_re = texts.lower()

    # 2. 슷자 제거
    texts_re2 = sub('\\d', '', texts_re)

    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = sub(punc_str, '', texts_re2)

    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = sub(spec_str, '', texts_re3)

    # 5. 공백 제거
    texts_re5 = sub('\s{2,}', ' ',texts_re4)
    return texts_re5

texts2 = [clean_text2(text) for text in texts]
print(texts2)



'''
추가 기록
'''

# match vs search
bool(match('ap','This is an apple')) # False : 문자열 시작부터 검색해 거짓이 나옴
bool(search('ap','This is an apple')) # True : 문자열 전체를 검색해 참이 나옴

# split : 대상 문자열에 괄호를 입력하면 분리 문자도 문자열에 포함됨
split('[0-9]+','사과 23 가격 20000 날짜 2020') # ['사과 ', ' 가격 ', ' 날짜 ', '']
split('([0-9]+)','사과 23 가격 20000 날짜 2020') # ['사과 ', '23', ' 가격 ', '20000', ' 날짜 ', '2020', '']

# 문자열 경계 변경하기
# 형식) '\b (문자열) \b', '패턴 \1 패턴', '문자열' -> '패턴 문자열 패턴'
sub(r'\b([0-9]{4}-[0-9]{4})\b', r'**\1**','1234-5678') # '**1234-5678**'



