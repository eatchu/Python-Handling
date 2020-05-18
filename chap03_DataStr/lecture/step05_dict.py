'''
dict 특징
 - set 구조와 유사함
 - R의 list와 구조가 유사함
 - key와 value 한 쌍으로 원소 구성
 - key 중복 불가, value 중복 가능
 형식) 변수 = {key1:value1, key2:value2, ... }
'''

# 1. dict 생성

# 방법1)
dic = dict(key1=100, key2=200, key3=300)
print(dic, len(dic), type(dic), sep='\n')

# 방법2)
dic2 = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(dic2)

# 2. 수정, 추가, 삭제, 검색 : key 이용

dic2['age'] = 45 # 수정1
dic2.update(age=35, pay=400) # 수정2 + 추가도 가능
dic2['pay'] = 350 # 추가1
dic2.setdefault('weight',50) #추가2
print(dic2)
# {'name': '홍길동', 'age': 45, 'addr': '서울시', 'pay': 350}
del dic2['addr'] # 삭제1
print(dic2) # {'name': '홍길동', 'age': 45, 'pay': 350}
dic2.pop('name') # 삭제2

# 키 검색
print('age' in dic2) # True
print(45 in dic2) # False 키 검색만 가능, value 검색 불가능


# 3. for 이용
for k in dic2 : # = dic2.keys()와 동일
    print(k, end='->') # key 값이 나옴
    print(dic2[k]) # value 값이 나옴

dic2.keys() # name age pay
dic2.values() # 홍길동 45 350
dic2.items() # (name,홍길동) (age,45) (pay,350)

for k, v in dic2.items() :
    print(k, end='->') # k = key
    print(v) # v = value

for d in dic2.items() :
    print(d) # tuple 형태로 값이 나옴
'''
('name', '홍길동')
('age', 45)
('pay', 350)
'''

# 4. key -> value
# 키를 이용해 값을 꺼내오는 두가지 방법
print(dic2['name'])
print(dic2.get('name'))


# 5. {'key':[value1,value2]} -> {'이름':[급여,수당]}
emp = {'홍길동':[250,50], '이순신':[350,80], 'yoo':[200,40]}
print(emp)
# 급여 250 이상인 경우 사원명, 수당 합계
su = 0
for k,v in emp.items() :
    if v[0] >= 250 :
       print(k,end='->')
       print(v)
       su += v[1]
print('수당 합계 =', su)


# 6. 문자 빈도수 구하기

charset = ['love','test','love','hello','test','love']
print(len(charset)) # 6

# 방법 1)
wc = {}
for word in charset :
    if word in wc :
        wc[word] += 1
    else :
        wc[word] = 1
print(wc)
# {'love': 3, 'test': 2, 'hello': 1}

print(max(wc,key=wc.get)) # love

# 방법 2)
wc2 = {}
for word in charset :
    wc2[word] = wc2.get(word,0) + 1
print(wc2)

# 해석
'''
love 키를 입력하고 love 키가 가지고 있는 값을 love키 안에 넣는다
하지만 love키가 처음 입력이 되어서 love키에 값이 존재하지 않는다면
0을 입력하고 다음에 love키가 다시 들어오게되면 원래 가지고 있던 값에 
+1 연산을 넣어 값을 늘려나간다
'''

l = {}
l['love'] = l.get('love', 1)
print(l) # {'love':1}
l['love'] = l.get('love') + 1
print(l) # {'love':2}