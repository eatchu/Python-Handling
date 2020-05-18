'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

print(findall('[가-힣]{3,}',emp)) # 왜 오류 뜸? 리스트 형식이라


names = []
for n in emp :
    nn = findall('[가-힣]{3}',n)
    if nn :
        names.append(nn[0])
print(names)


# list + for 이용한 경우

names = [findall('[가-힣]{3}',n)[0] for n in emp]
print(names)



