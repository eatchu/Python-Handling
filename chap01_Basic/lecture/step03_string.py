'''
문자열 처리
- 문자열(string) : 문자들의 순서(index) 집합
- indexing/slicing 기능
- 문자열 = 상수 : 수정 불가
'''

# 1. 문자열 처리

# 문자열 유형
lineStr = 'this is one ling string' # 한 줄 문자열
print(lineStr)

# 줄바꿈사용 (''') or (\n)
multiStr = '''this
is multi line
string'''
print(multiStr)

multiStr2 = 'this \nis multi line\nstring'
print(multiStr2)

# sql문 : 부서번호
deptno = int(input('부서번호 입력 :'))
query = f'''select * from emp 
where deptno = {deptno}
order by sel desc'''
print(query)


# 2. 문자열 연산 (+결합, *반복)
print('python'+' program') # python program
print('python ' + str(3.7)) # python 3.7
print('-'*15) # ---------------

'''
object.member or object.member()
int.member
str.member
'''


# 3. 문자열 처리 함수
lineStr = 'this is one ling string'
print(lineStr, type(lineStr))
# this is one ling string <class 'str'>
print('문자열 길이 : ', len(lineStr)) # 23
print('t의 글자수 : ', lineStr.count('t')) # 2 : t가 몇개있는지
print('t가 처음나온 위치 :', lineStr.find('t')) # 0 : t는 제일 처음 나옴
print('t가 처음나온 위치 :', lineStr.index('t')) # 0
print('z가 처음나온 위치 :', lineStr.find('z')) # -1 : z 안나옴
print('s가 처음나온 위치 :', lineStr.find('s')) # 3 : s는 4번째에 나옴
print(lineStr.rfind('t'))  # 18 : 제일 마지막에 나온 t의 위치


# 접두어 : 시작문자열
lineStr.startswith('this') # True : 문자열이 this로 시작했는지 논리값 반환
lineStr.startswith('that') # False

# 문장 -> 문단
multiStr = '''this
is multi line
string'''
sentence = multiStr.split(sep='\n')
print(sentence) # ['this', 'is multi line', 'string']

# split : 토큰 생성
words = lineStr.split(sep=' ') # 문장 -> 단어
print(words) # ['this', 'is', 'one', 'ling', 'string']
print('단어길이 :', len(words)) # 단어길이 : 5

# 문단 결합 (join) -> 문장 : '구분자'.join(str)
sentence = ' '.join(words)
print(sentence)  # this is one ling string
para = '\n'.join(sentence)
print(para)

# 소문자 대문자
multiStr.lower()
multiStr.upper()
multiStr.swapcase() # 서로 교환

# indexting/scling
print(lineStr[0]) # 첫번째 문자 t
print(lineStr[-1]) # 마지막 문자 g
print(lineStr[0:4]) # [start:end-1] this
print(lineStr[-6:]) # 오른쪽 끝 6개 문자열 string


# 4. escape 문자 처리
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



