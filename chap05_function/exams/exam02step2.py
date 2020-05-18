'''
문2-2) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <출력 결과>
 전체 사원 급여 평균 : 260
'''

from re import findall, sub
from statistics import mean


'''
111
'''

# <Vector 준비>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의

def pay_pro(emp):
    sal = 0
    cnt = 0
    for e in emp :
        cnt += 1
        sal += int(findall('\d{3}$', e)[0][0:3])
    print('총급여=',sal)
    money = sal/cnt
    return money

# 함수 호출 
pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)


'''
222
'''


emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
def pay_pro(emp):
    sal = []
    for e in emp:
        sal.append(int(findall('\d{3}$', e)[0][0:3]))
    return mean(sal)

# 함수 호출
pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)




'''
333
'''
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
def pay_pro(emp) :
    sal = []
    for e in emp :
        sal.append(findall('\d{3}$',e)[0])
        sal = list(map(int, sal))
    return mean(sal)

# 함수 호출
pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)




# map 함수 사용 예시

emp2 = ["201420", "200300", "2010260"]
a = map(int, emp2)
b = list(map(int, emp2))
print(a,b)
'''
a(map 함수만 사용) : map object가 만들어짐
b(list(map)을 사용) : 숫자형으로 변환된 리스트 형태가 만들어짐
'''



