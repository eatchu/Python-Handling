'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd

# 1. file read
emp = pd.read_csv('./chap07_File_IO/data/emp.csv', encoding='utf-8')
print(emp.info())
print('관측치 길이 :', len(emp))
pay = emp.Pay
name = emp.Name

# 방법 1
max_name = [name[i] for i in range(len(pay)) if pay[i] == max(pay)]
min_name = [name[i] for i in range(len(pay)) if pay[i] == min(pay)]

print('전체 평균 급여 : ', pay.mean())
print('='*20)
print('최저 급여 : %d, 이름 : %s'%(min(pay), max_name[0]))
print('최고 급여 : %d, 이름 : %s'%(max(pay), min_name[0]))
print('='*20)


# 방법 2
print('='*20)
for i,p in enumerate(pay) :
    if p == min(pay) :
        print('최저급여 : %d, 이름 : %s'%(p,name[i]))
    elif p == max(pay) :
        print('최고급여 : %d, 이름 : %s'%(p,name[i]))
print('=' * 20)



# 추가
# emp.Name[emp['Pay']==min(pay)] # 최저 급여를 받는 사람의 이름만 꺼내오기
# emp.Name[emp['Pay']==max(pay)] # 최고 급여를 받는 사람의 이름만 꺼내오기