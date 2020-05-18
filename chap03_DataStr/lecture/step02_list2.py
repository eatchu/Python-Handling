'''
리스트 내포
 - list에서 for문 사용하는 법
 형식1) 변수 = [실행문 for 변수 in 열거형객체]
       실행순서 : 1 for문 > 2 실행문 > 3 변수저장
 형식2) 변수 = [실행문 for 변수 in 열거형 객체 if 조건식]
       실행순서 : 1 for문 > 2 if문 > [3 실행문 > 4 변수저장]
'''

# 형식1) 변수 = [실행문 for 변수 in 열거형객체]
x = [2,4,1,3,7]
# (1) x각 변량에 제곱 취하기
data = []
for i in x :
    data.append(i**2)
print(data)

# (2) 간소화하게 제곱 취하기
data2 = [i**2 for i in x]
print(data2)


# 형식2) 변수 = [실행문 for 변수 in 열거형 객체 if 조건식]

# 1~100 -> 3의 배수만 선택
num = list(range(1,101))
data3 = [i for i in num if i % 3 == 0]
print(data3)

# 내장함수 + 리스트 내포 결합
sum(x) # 17
data4 = [[1,3,5],[4,5],[7,8,9]] # 중첩리스트
result = [sum(d) for d in data4]
print(result) # 9 9 24























