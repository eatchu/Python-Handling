'''
< 작업 순서 >
1. index 페이지 작성 -> 검색할 동 입력
2. flask server 에서 동(파라미터 형식) 받기
3. DB 연동 -> 해당 동 주소 조회
4. 조회 결과 -> result 페이지 출력
'''


from flask import Flask, render_template, request

app = Flask(__name__)


# 함수 장식자
@app.route('/') # 기본 url 요청 -> 함수 호출
def index() :
    return render_template('/app03/index.html')
@app.route('/search', methods=['GET','POST'])
def search() :
    if request.method == 'POST' :
        dong = request.form['dong'] # 사용자가 입력한 동을 받음
        # print('dong=',dong)

        import pymysql
        config = {
            'host': '127.0.0.1',
            'user': 'scott',
            'password': 'tiger',
            'database': 'work',
            'port': 3306,
            'charset': 'utf8',
            'use_unicode': True}

        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()

            # 레코드 조회 및 레코드 추가
            sql = "select * from zipcode_tab"
            cursor.execute(sql)
            data = cursor.fetchall()

            if data:  # True : 검색
                '''
                for row in data:
                    print("[%s]    %s   %s   %s  %s" % row)

                print('전체 레코드 수 : ', len(data))
                '''

                ### 1. 동 검색
                # dong = input("검색할 동 입력 :")
                sql = f"select * from zipcode_tab where dong like '%{dong}%'"
                cursor.execute(sql)
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print("[%s]    %s   %s   %s  %s" % row)

                    # print('검색된 레코드 수:', len(data2))
                    size = len(data2)
                else:
                    print('검색된 레코드 없음')

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    return render_template('/app03/result.html', dong=dong, data= data2, size = size)


if __name__ == "__main__":
    app.run(host='192.168.12.6')

