'''
문제2) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 2 350000
4 HDTV 2 1500000
전체 레코드 수 : 4

    [ 상품별 총금액 ]
냉장고 상품의 총금액은 1,700,000
세탁기 상품의 총금액은 1,650,000
전자레인지 상품의 총금액은 700,000
HDTV 상품의 총금액은 3,000,000
'''

import sqlite3

try :
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")
    cursor = conn.cursor()

    # 테이블 레코드 수정
    cursor.execute("update goods set dan=850000 where code=1")
    cursor.execute("update goods set dan=550000 where code=2")
    cursor.execute("update goods set dan=350000, su=2 where code=3")
    cursor.execute("update goods set dan=1500000 where code=4")
    conn.commit()

    # 현재 goods 테이블 현황 출력
    print('[ goods 테이블 현황 ]')
    cursor.execute("select*from goods")
    data = cursor.fetchall()
    for row in data:
        print('%d \t %s \t %d \t %d' % (row))
    # for row in data :
       # print('%s 상품의 총 금액은 '%(row[1]), format(row[2]*row[3],'3,.0f'))

    # sql 연산으로 사용하기
    print('[ 상품별 총금액 ]')
    sql = 'select name, dan*su from goods'
    cursor.execute(sql)
    data2 = cursor.fetchall()
    for row in data2 :
        print('%s 상품의 총 금액은 '%(row[0]), format(row[1],'3,.0f'))


except Exception as e :
    print('db 오류 :', e)

finally:
    cursor.close()
    conn.close()

