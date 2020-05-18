'''
emp join dept

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
    # 1. ANSI inner join
    sal = int(input('급여:')) # 250
    sql = f""" select e.eno, e.ename, e.sal, d.dname
    from emp e inner join dept d
    on e.dno = d.dno and e.sal >= {sal}"""
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0],row[1],row[2],row[3])

    # 2. subquery : 부서번호(dept) -> 사원정보(emp)
    dno = int(input('부서번호 입력')) # 10
    sql = f"""select eno, ename, hiredate, dno from emp 
    where dno = (select dno from dept where dno = {dno})"""
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0],row[1],row[2],row[3])
    print('해당 부서 사원 수 :',len(data))

    # 문제) subquery2 : 사원이름(ename) -> 부서정보(dname) 출력
    name = input('사원이름')
    sql = f"""select e.ename, d.dname, d.dno from dept d inner join emp e
    where d.dno = e.dno and e.ename like '%{name}%'"""
    cursor.execute(sql)
    data = cursor.fetchall()
    if data :
        for row in data :
            print(row[0],row[1],row[2])
    else:
        print('해당 사원 없음')


except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()

