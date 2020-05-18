'''
step01 list
- 인덱스 사용가능
- 추가 삽입 삭제 수정 가능
- 자체 연산 불가능 (for문 사용해야함)
'''

# 값 수정 (추가, 수정, 삽입, 삭제, 정렬)
num = ['one','two','three','four']
num.append('five') # 원소 추가 : ['one','two','three','four','five']
num.remove('five') # 원소 삭제 1
del num[3] # 원소 삭제 2 : ['one','two','three','four']
num.insert(0,'zero') # 특정 위치 원소 삽입 (idx,값) : ['zero', 'one', 'two', 'three', 'four']
result = [1,2,3,4]*3
result.sort()
result.sort(reverse=True)


# append vs extend
'''
append : 변수 or 값 자체를 그대로 넣는다
extend : 원소 하나하나를 넣는다
         리스트라면 인덱스 단위마다 삽입, 문자열이라면 글자마다 삽입됨
'''
x = [1,2,3,4]
y = [1.5,2.5]
x.extend(y) # [1,2,3,4,1.5,2.5]
x.append(y) # [1,2,3,4,[1.5,2.5]]
x.extend('dueui') # 'd', 'u', 'e', 'u', 'i'
x.append('dueui') # 'dueui'


'''
step02 list 한줄 정렬
'''

# 형식1) 변수 = [실행문 for 변수 in 열거형객체]
x = [2,4,1,3,7]
# x각 변량에 제곱 취하기
double = [i**2 for i in x]
print(double)

# 형식2) 변수 = [실행문 for 변수 in 열거형 객체 if 조건식]
# 1~100 -> 3의 배수만 선택
thr = [i for i in range(1,101) if i%3==0]
print(thr)

'''
step03 tuple
 - index 사용가능 
 - 수정, 추가, 삽입, 삭제 불가능
 - 관련 함수 없음
'''

# 최댓값/최솟값 구하기
val = [34,5,104,56,78,33,2,40]
xma = nmi = val[0]
for i in val :
    if xma < i :
        xma = i
    elif nmi > i :
        nmi = i
print('최댓값 :',xma,'최솟값 :',nmi )


'''
step04 set
 - 인덱스 사용 불가
 - 중복 허용 불가
'''

# 중복을 허용하지 않음
s = {1,3,5,1,5} # 1 3 5

# 집합 관련 함수
s2 = {3,6}
print(s.union(s2)) # 합집합 : 1 3 5 6
print(s|s2) # 합집합
print(s.difference(s2)) # 차집합 : 1 5
print(s-s2) # 차집합
print(s.intersection(s2)) # 교집합 : 3
print(s&s2) # 교집합

# list vs gender
gender = ['남자', '여자', '남자', '여자']
print(set(gender)) # {'남자', '여자'}

# 원소 추가/삭제
s3 = {1,3,5,7}

s3.add(9) # 원소 추가 1 3 5 7 9
s3.discard(3) # 원소 삭제 1 5 7 9

'''
step05 dictionary
'''

# dict 생성법
# 방법1)
dic = dict(key1=100, key2=200, key3=300)
# 방법2)
dic2 = {'name':'홍길동', 'age':35, 'addr':'서울시'}


# 수정, 추가, 삭제, 검색 : key 이용
dic2['age'] = 45 # 수정1
dic2['pay'] = 350 # 추가1
dic2.update(age=35, pay=400) # 수정2 + 추가도 가능
dic2.setdefault('weight',50) #추가2
# {'name': '홍길동', 'age': 45, 'addr': '서울시', 'pay': 350}
del dic2['addr'] # 삭제1
dic2.pop('name') # 삭제2

# 키 검색
print('age' in dic2) # True
print(45 in dic2) # False 키 검색만 가능, value 검색 불가능

# 키를 이용해 값을 꺼내오는 두가지 방법
print(dic2['name'])
print(dic2.get('name'))



#  문자 빈도수 구하기 : 과제 !
charset = ['love','test','love','hello','test','love']
count = {}
for word in charset :
    count[word] = count.get(word,0)+1
print(count)
