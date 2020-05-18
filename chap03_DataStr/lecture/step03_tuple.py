'''
tuple 특징
 - index 사용, 순서 존재
 - 1차원 배열 구조
 - 수정 불가, 처리 속도 빠름
 - 제공 함수 없음
 형식) 변수 = (원소1, 원소2, ...)
'''

tp = 10 # scala
tp1 = (10)
print(tp,tp1) # 10 10

tp2 = (10,)
print(tp2, type(tp2)) # (10,) <class 'tuple'>

# index 동일하게 사용가능
tp3 = (10,58,4,96,55,2)
print(tp3[:4]) # (10, 58, 4, 96)
print(tp3[-3:]) # (96, 55, 2)

# 수정 불가능
# tp3[0] = 100 TypeError

# max/min
vmax = vmin = tp3[0]
for t in tp3 :
    if vmax < t :
        vmax = t
    else :
        vmin = t
print('최댓값=',vmax) # 96
print('최솟값=',vmin) # 2

max(tp3) # 96
min(tp3) # 2


# list = tuple
lst = list(range(10000))
print(len(lst)) # 10000
print(type(lst)) # list

tlst = tuple(lst)
print(type(tlst)) # tuple

# tuple 대입 연산
student1 = (" 철수 ", 19, "CS")
(name, age, major) = student1
'''
name -> ' 철수 ' 
age -> 19 
major -> 'CS’ 
'''








