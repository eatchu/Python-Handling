'''
반복문(for)
형식)
for 변수 in 열거형객체 :
    실행문
    실행문

열거형객체(iterable) : string, list, tuple, set/dict
제너레이터 식 : 변수 in 열거형객체
'''

# 1. string 열거형 객체 이용
string = '나는 홍길동 입니다.'
print(len(string)) # 11

for s in string : # 11번 반복됨
    print(s, end='') # 나는 홍길동 입니다.

for s in string.split(' ') :
    print(s)
# 나는
# 홍길동
# 입니다.


# 2. list 열거형 객체 이용
help(list)
lst = [1,2,3,4,5]
print(lst) # object 내용
print(type(lst)) # object 자료형

lst2 = []
for i in lst :
    print(i,end=' ')
    lst2.append(i**2)
print('\n',lst2)

'''
list 자체로 연산을 할 수 없음
ex) lst = lst** -> error
for문을 사용하여 원소를 하나씩 가져와 연산을 수행해야함
'''

# 1~100 원소를 갖는 list 객체 생성
print(list(range(100))) # 0~99
print(list(range(1,101))) # 1~100


# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수
range(start,stop) : start ~ stop-1 정수
range(start,stop,step) : start ~ stop-1, step 정수
'''
num1 = range(10) # 0~9
num2 = range(1,10) # 2~9
num3 = range(1,10,2) # 1 3 5 7 9
print(num1,'\n',num2,'\n',num3)

for i in num1 :
    print(i, end=' ')
print()
for i in num2 :
    print(i, end=' ')
print()
for i in num3 :
    print(i, end=' ')


# 4. list + range 열거형 객체 이용
idx = range(5)
print(idx) # range(0, 5)
idx = list(range(5))
print(idx) # [0, 1, 2, 3, 4]


# 문제) 1~100까지 100개의 원소를 갖는 vector를 생성하고
#      3의 배수만 저장하기 (방법 2가지)
lst1 = list(range(1,101))
lst2 = list(range(3,101,3))
print(lst1)
print(lst2)
lst3 = []
for i in lst1 :
    if i%3 == 0 :
        lst3.append(i)
print(lst3)

# index 이용 : 분류정확도
y = [1,0,2,1,0] # 관측치 : 범주형(0,1,2)
y_pred = [1,0,2,0,0] # 예측치

size = len(y)
acc = 0
for i in range(size) :
    fit = int(y[i]==y_pred[i]) #int(True/False) => 1/0
    acc += fit * 20
print('분류정확도 =',acc)


# 5. 이중 for문
for i in range(2,10) :
    print('***%d단***'%(i))
    for j in range(1,10) :
        print('%dx%d=%d'%(i,j,(i*j)))
    print('\n') #라인 스킵


para = '''나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다.'''

# 문자열 처리
sents = []
words = []
for sent in para.split('\n') : # 문장 -> 문단
    sents.append(sent)
    for word in sent.split() : # 문단 -> 단어
        words.append(word)
print(sents)
print(words)


# 제너레이터 식 : 변수 in 열거형 객체
'''
for 변수 in 열거형 객체 :
    -> 객체의 원소 수 만큼 반복
if 값 in 열거형 객체 :
    -> 객체 원소안에 값이 있으면 True, 아니면 False 반환
'''
search = input('검색 단어 입력 : ')
if search in words :
    print('해당 단어 있음')
else :
    print('해당 단어 없음')




