'''
문제3) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
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
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 :
            selec = int(input('조회 방법 1.전체조회 2.상품조회:'))
            if selec == 1 :
                cursor.execute("select*from goods")
                data = cursor.fetchall()
                for row in data:
                    print('code%d. %s 갯수%d 가격%d'%(row[0],row[1],row[2],row[3]))
            elif selec ==2 :
                cursor.execute("select name from goods")
                n = cursor.fetchall()
                print(n)
                name = input('상품명 조회:')
                sql = f"select * from goods where name like '%{name}%'"
                cursor.execute(sql)
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print('code%d. %s 갯수%d 가격%d'%(row[0],row[1],row[2],row[3]))
                else:
                    print('조회 상품 없음')

        elif menu == 2:
            code = int(input('code:'))
            name = input('name:')
            su = int(input('su:'))
            dan = int(input('dan:'))
            sql = f"insert into goods values({code},'{name}',{su},{dan})"
            cursor.execute(sql)
            conn.commit()

        elif menu == 3:
            new = int(input('1.단가 변경 2.수량 변경 :'))
            if new == 1:
                name = input('변경할 상품명 입력 :')
                dan = int(input('수정 단가:'))
                sql = f"update goods set dan={dan} where code like '%{code}%'"
                cursor.execute(sql)
                conn.commit()
            elif new == 2:
                name = input('변경할 상품명 입력 :')
                su = int(input('수정 수량:'))
                sql = f"update goods set su={su} where code like '%{code}%'"
                cursor.execute(sql)
                conn.commit()

        elif menu == 4:
            code = int(input('삭제 code:'))
            cursor.execute(f"select*from goods where code={code}")
            row = cursor.fetchone()
            if row:
                cursor.execute(f"delete from goods where code={code}")
            else:
                print('해당 코드 없음')

        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 exit
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
