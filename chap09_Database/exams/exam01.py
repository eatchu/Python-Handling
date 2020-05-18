'''
문제1) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
 <조건1> 전자레인지 수량, 단가 수정 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 5  600000 <- 수량, 단가 수정
4 HDTV 2 1500000  <- 수량 수정
전체 레코드 수 : 4
'''
import sqlite3

try :
    # 현재 goods 테이블 현황 출력
    conn = sqlite3.connect("./chap09_Database/data/sqlite.db")
    cursor = conn.cursor()
    cursor.execute("select*from goods")
    data = cursor.fetchall()
    for row in data :
        print('%d \t %s \t %d \t %d'%(row))
    # 테이블 수정
    cursor.execute("update goods set dan=600000, su=5 where code=3")
    cursor.execute("update goods set su=2, name='HDTV' where code=4")
    conn.commit()


except Exception as e :
    pass

finally:
    cursor.close()
    conn.close()



