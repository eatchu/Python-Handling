'''
sqlite3
 - 내장형 DBMS : 기기 내부에서 사용
 - 외부 접근 허용 안됨
 - 쿼리문을 작성할때는 항상 "쌍따움표" 사용
'''

import sqlite3

print(sqlite3.sqlite_version_info) # (3, 31, 1)

try :
    # 1. database 생성 & db 연동 객체 생성
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")
    # sql문 실행 객체
    cursor = conn.cursor() # 쿼리문 실행 객체

    # 2. table 생성
    sql = """create table if not exists test_tab(name text(10),
    phone text(15), addr text(50))"""
    cursor.execute(sql) # db와 연동해 table을 생성해줌

    # 3. 레코드 추가
    '''
    cursor.execute("insert into test_tab values('홍길동','010-111-1111','서울시')")
    cursor.execute("insert into test_tab values('이순신','010-111-1111','해남시')")
    cursor.execute("insert into test_tab values('유관순','010-111-1111','충남')")
    conn.commit() # 추가된 레코드 최종 db에 반영
    '''

    # 4. 레코드 조회
    cursor.execute("select * from test_tab") # cursor 객체에 레코드들이 저장되어 있음
    dataset = cursor.fetchall() # 객체 레코드 -> 레코드 가져오기
    for row in dataset :
        print(row) # tuple : ('홍길동', '010-111-1111', '서울시')

    print('이름 \t 전화번호 \t 주소')
    for row in dataset :
        print(row[0]+'\t'+row[1]+'\t'+row[2]) # 홍길동	010-111-1111	서울시

except Exception as e :
    print('db 연동 오류 :', e)
    conn.rollback() # 이전 쿼리 실행 취소

finally :
    cursor.close()
    conn.close()


