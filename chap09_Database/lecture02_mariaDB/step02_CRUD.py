'''
CRUD
 - Create, Read, Update, Delete
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
    # 1. db 연동 객체
    conn = pymysql.connect(**config)

    # 2. cursor 객체 : sql문
    cursor = conn.cursor()

    # 4. Insert
    '''
    code = int(input('code:'))
    name = input('name:')
    su = int(input('su:'))
    dan = int(input('dan:'))
    sql = f"insert into goods values({code},'{name}',{su},{dan})"
    cursor.execute(sql)
    conn.commit()
    '''
    '''
    # 5. update
    code = int(input('수정 code:'))
    su = int(input('수정 su:'))
    dan = int(input('수정 dan:'))
    sql = f"update goods set su={su}, dan={dan} where code={code}"
    cursor.execute(sql)
    conn.commit()
    '''

    # 6. Delete
    code = int(input('삭제 code:'))
    cursor.execute(f"select*from goods where code={code}")
    row = cursor.fetchone()
    if row:
        cursor.execute(f"delete from goods where code={code}")
    else:
        print('해당 코드 없음')

    # 3. Read(Select)
    # 전체 검색
    cursor.execute("select*from goods")
    data = cursor.fetchall()
    for row in data :
        print(row[0],row[1],row[2],row[3])

    '''        
    # 상품명 검색
    name = input('상품명 조회:')
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)
    data2 = cursor.fetchall()
    if data2:
        for row in data2 :
            print(row)
    else:
        print('조회 상품 없음')
    # 상품 코드 검색
    code = int(input('조회할 코드 입력:'))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    data2 = cursor.fetchone()
    if data2:
        print(data2)
    else:
        print('조회 상품 없음')
    '''

except Exception as e:
    print('db 연동 에러 :',e)
finally:
    pass






