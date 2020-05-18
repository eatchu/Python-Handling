scores = [ ]
for i in range(10):
    scores.append(int(input(" 성적을입력하시오 :")))

print(scores)

scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]
print(scores)
scores[0] = 80; # 특정 위치 값 수정
scores[1] = scores[0]; # 특정 위치 값에 특정 위치 값을 복사

rows = 4
cols = 3

s = []
for row in range(rows):
    s += [[0] * cols]

print("s =", s)
# s =  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

len(s[0]) # 열
len(s) # 행





# list.expend 와 list.append의 차이


# 구조별 object.method() 정리
# list
num.append('five') # 원소 추가
num.remove('five') # 원소 삭제 1
del num[3] # 원소 삭제 2
num.insert(0,'zero') # 특정 위치 원소 삽입 (idx,값)
num[0] = 0 #원소 수정
x.extend(y)
x.append(y)
result.sort() # 정렬
sorted(result) # 값이 바로 나오게 정렬
result.sort(reverse=True)

# tuple (수정x,삽입x,삭제x)

# set (중복x, 인덱스x)
s3 = {1,3,5,7}
s3.add(9) # 원소 추가
s3.discard(3) # 원소 삭제
s = {1,3,5,1,5}
s2 = {3,6}

print(s.union(s2)) # 합집합 : 1 3 5 6
print(s|s2) # 합집합

print(s.difference(s2)) # 차집합 : 1 5
print(s-s2) # 차집합

print(s.intersection(s2)) # 교집합 : 3
print(s&s2) # 교집합

# dict
dic2.keys() # 키
dic2.values() # 값
dic2.items() # (키,값)



