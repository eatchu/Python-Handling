'''
table 전체 조회 -> 생성 및 조회
1. table이 없는 경우 table 생성
2. table이 있는 경우 table 조회
- 테이블 유무에 따른 선택적 프로그램
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

    # 1. 전체 table 조회 : 테이블 유무 확인
    cursor.execute("show tables")
    tables = cursor.fetchall()
    sw = False # 스윗징 기법
    if tables: # 테이블의 존재 유무
        for tab in tables:
            print(tab[0]) # 존재하는 테이블명 출력
            if tab[0] == 'emp':
                sw = True
    if sw == False: # 테이블 생성
        print('emp table 없음')
        sql = """create table emp (
        eno int auto_increment primary key,
        ename varchar(20) not null,
        hiredate date not null,
        sal int,
        bonus int default 0,
        job varchar(20) not null,
        dno int)"""
        cursor.execute(sql)
        sql2 = "alter table emp auto_increment = 1001"
        cursor.execute(sql2)
        sql3 = """insert into emp(ename, hiredate, sal, bonus, job, dno)
        values('홍길동','2010-10-20',300, 35, '관리자', 10)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
        values('강호동','2015-09-20',250, '사원', 20)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
        values('유관순','2020-10-20',220, '사원', 10)"""
        cursor.execute(sql3)
        conn.commit()
    else: # 테이블 조회
        # 전체 레코드 조회
        print('emp table 있음')
        cursor.execute("select*from emp")
        data = cursor.fetchall()
        for row in data:
            print(row)
        print('전체 레코드 수 :', len(data))

        # 사원 조회
        name = input('사원이름:')
        sql = f"select eno, ename, dno from emp where ename = '{name}'"
        cursor.execute(sql)
        data2 = cursor.fetchall()
        if data2:
            print(data2[0])
        else:
            print('해당사원 없음')

        '''      
        # 문제) 사원 수정 : 키보드(사번,급여,보너스) -> 급여, 보너스 수정
        no = int(input('사번 입력'))
        sal = int(input('급여 입력'))
        bonus = int(input('보너스 입력'))
        sql = f"update emp set sal={sal},bonus={bonus} where eno={no}"
        cursor.execute(sql)
        conn.commit()

        # 문제) 레코드 삭제 : 키보드(사번) -> 검색(유무) -> 레코드 삭제 or 없음
        no = int(input('사번 입력'))
        cursor.execute(f"select*from emp where eno={no}")
        data = cursor.fetchall()
        if data:
            cursor.execute(f"delete from emp where eno={no}")
        else:
            print('해당 사원번호 없음')'''


except Exception as e:
    print('db 오류:',e)
finally:
    cursor.close()
    conn.close()









