'''
group by 집단변수(범주형)
'''

import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 1. 부서, 2. 직책
    gcol = int(input('1. 부서별, 2. 직책별'))
    if gcol == 1:
        sql = """select dno, sum(sal), round(avg(sal),2) from emp 
        group by dno order by dno"""
    elif gcol == 2:
        sql = """select job, sum(sal), round(avg(sal),2) from emp
        group by job order by job"""
    else:
        print('잘못입력')
    # sql 실행 -> 검색 결과 출력하기
    cursor.execute(sql)
    data = cursor.fetchall()
    gcol = "부서" if gcol == 1 else "직책"
    print('%s  급여합계  급여평균'%(gcol))
    for row in data:
        print(row[0],'\t', row[1],'\t', row[2])

except Exception as e:
    print(e)
finally:
    pass

