'''
CRUD
 - Create, Read, Update, Delete
'''

import sqlite3

try:
    # 1. db 연동 객체 생성
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. table 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0)"""
    cursor.execute(sql) # table 생성

    # 3. 레코드 추가
    '''
    cursor.execute("insert into goods values(1, '냉장고', 2, 85000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 55000)")
    cursor.execute("insert into goods(code,name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code,name,dan) values(4, 'HDTV', 85000)")
    conn.commit()

    # 레코드 수정
    cursor.execute("update goods set dan = 150000 where name = 'HDTV'")
    conn.commit()
    '''

    code = int(input('코드 입력:'))
    name = input('상품명 입력:')
    su = int(input('수량 입력:'))
    dan = int(input('단가 입력:'))

    sql = f"insert into goods values({code},'{name}',{su},{dan})"
    cursor.execute(sql)
    conn.commit()


    # 4. 1) 레코드 조회
    cursor.execute("select*from goods")
    data = cursor.fetchall()
    for row in data :
        # print(row[0],row[1],row[2],row[3])
        print('%d  %s  %d  %d'%(row))
    print('전체 레코드 수 :', len(data))

    #    2) 레코드 조건식 조회
    cursor.execute("select * from goods where su >= 2")
    data = cursor.fetchall()
    for row in data :
        print('%d  %s  %d  %d'%(row))
    print('전체 레코드 수 :', len(data))

    #    3) 키보드 입력 -> 검색
    name = input("검색할 상품명 입력 :")
    cursor.execute(f"select * from goods where name like '%{name}%'")
    dataset = cursor.fetchall()
    # 검색 레코드가 없는 경우 대비
    if dataset :
        for row in dataset:
            print('%d  %s  %d  %d' % (row))
        print('검색된 레코드 수 :', len(dataset))
    else :
        print('검색된 레코드 없음')


    # 5. 레코드 수정
    '''
    sql = "update goods set name = '테스트' where code = 4"
    cursor.execute(sql)
    conn.commit()
    
    code = int(input('수정 코드 입력:'))
    su = int(input('수정 수량 입력:'))
    dan = int(input('수정 단가 입력:'))
    sql = f"update goods set su={su}, dan={dan}, where code={dan}"
    cursor.execute(sql)
    conn.commit()
    

    # 6. 레코드 삭제
    code = int(input('삭제할 코드 입력 :'))
    sql = f"delete from goods where code = {code}"
    cursor.execute(sql)
    dataset = cursor.fetchall()

    if dataset :
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)
        conn.commit()
    else :
        print('해당 코드 없음')
    '''


except Exception as e:
    print('db 연동 오류 :', e)
finally:
    cursor.close()
    conn.close()




