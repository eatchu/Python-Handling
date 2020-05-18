'''
list 특징
 - 1차원 배열구조
   형식) 변수 = [값1,값2,...]
 - 다양한 자료형 저장 가능
 - index 사용 : 각 데이터에 순서가 존재
   형식) 변수[idx], index=0,1,2...
 - 값 수정 가능 (추가, 삽입, 수정, 삭제)
'''


# list 생성하는 법 : 구글링
a = input().split()




# 1. 단일 list
lst = [1,2,3,4,5]
print(lst, type(lst), len(lst))

for i in lst :
    # print(i, end=' ')
    print(lst[i-1: ])
'''
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
'''

for i in lst :
    # print(i, end=' ')
    print(lst[ :i])
'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
'''





'''
index 형식
변수[start:stop:step]
'''
x = list(range(1,101))


print(x[0],x[-1]) # 1 100
print(x[:5]) # 1 2 3 4 5
print(x[-5:]) # 96 97 98 99 100
print(x[:]) # 전체 데이터 출력
print(x[0:10:2]) # 1 3 5 7 9
print(x[::2]) # 1 3 5 7 ... 97 99 홀수 출력
print(x[1::2]) # 2 4 6 8 ... 98 100 짝수 출력


# 2. 중첩 list : [[],[]]
a = ['a','b','c']
b = [10,20,5,True,'hong'] # 여러가지 type 저장 가능
print(b)
print(type(b[3]),type(b[1]))

b = [10,20,5,a,True,'hong'] # a 리스트를 값에 추가
print(b) # [10, 20, 5, ['a', 'b', 'c'], True, 'hong']
print(b[3]) # ['a', 'b', 'c']
print(b[3][2]) # c


# 3. 값 수정 (추가, 수정, 삽입, 삭제)
num = ['one','two','three','four']
print(len(num))

num.append('five') # 원소 추가
print(num)
num.remove('five') # 원소 삭제 1
print(num)
del num[3] # 원소 삭제 2
print(num)
num.insert(0,'zero') # 특정 위치 원소 삽입 (idx,값)
print(num) # ['zero', 'one', 'two', 'three', 'four']
num[0] = 0 #원소 수정
print(num) # [0, 'one', 'two', 'three', 'four']


# 4. list 연산 (+,*)

# 1) list 결합 (+)
x = [1,2,3,4]
y = [1.5,2.5]
z = x + y # 결합
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# 2) list 확장
x.extend(y)
print(x)

# 3) list 추가
x.append(y)
print(x)

# 4) list 곱셈(*)
lst = [1,2,3,4]
result = lst * 3
print(result)



# 5. list 정렬
result.sort()
print(result)

result.sort(reverse=True)
print(result)



# 6. scala vs vector

'''
scala 변수 : 한 개의 상수(값)를 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기, 방향)
'''

dataset = [] # 빈 list : vector
size = int(input('vector size :')) # 5 입력

for i in range(size) :
    dataset.append(i) # vector 변수 생성됨

print(dataset) # 0 1 2 3 4


# 7. list에서 원소 찾기
'''
if 값 in list :
   참 실행문
else :
   거짓 실행문
'''

if 5 in dataset :
    print("5가 있음")
else :
    print("5가 없음")








