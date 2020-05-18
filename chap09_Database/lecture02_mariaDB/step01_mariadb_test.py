'''
MariaDB 연동 TEST
'''

import pymysql

print(pymysql.version_info) # (1, 3, 12, 'final', 0)

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}


try :
    # 1. db 연동 객체 생성
    conn = pymysql.connect(**config)

    # 2. sql 실행 객체 생성
    cursor = conn.cursor()

    # 3. table 생성
    '''
    sql = """create table goods(
    code int pirmary key,
    name varchar(30) not null,
    su int not null,
    dan int not null)"""
    cursor.execute(sql)
    
    # 3. 레코드 추가
    
    cursor.execute("insert into goods values(1, '냉장고', 2, 85000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 55000)")
    cursor.execute("insert into goods(code,name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code,name,dan) values(4, 'HDTV', 85000)")
    conn.commit()
    '''

    # 4. sql문 실행
    sql = "select*from goods"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    for row in dataset :
        print(row[0],row[1],row[2],row[3])
    print('전체 레코드 수 :', len(dataset))

except Exception as e :
    print('db 오류:',e)
finally:
    pass
