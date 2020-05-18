'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(sql 폴더)
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pandas as pd 

# 칼럼 단위 읽기 
emp = pd.read_csv("./chap09_Database/data/emp.csv", encoding='utf-8')
print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
print(no, name, pay)

    
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
    tab = conn.cursor()

    # 테이블 생성
    sql = """create table emp(
    eno int auto_increment primary key,
    ename varchar(30) not null,
    sal int not null)"""
    tab.execute(sql)

    # 레코드 추가
    for i in range(5):
        eno = no[i]
        ename = name[i]
        sal = pay[i]
        sql = f"""insert into emp values({eno},'{ename}',{sal})"""
        tab.execute(sql)
    conn.commit()

    # 테이블 조회
    tab.execute("select * from emp")
    data = tab.fetchall()
    for row in data:
        print(row[0],row[1],row[2])


except Exception as a:
    print('오류 발생:',a)
finally:
    tab.close()
    conn.close()


