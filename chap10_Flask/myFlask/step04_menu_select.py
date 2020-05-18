'''
get vs post
 - 파라미터 전송 방식
 - get : url에 노출(소량)
 - post : body에 포함되어 변수를 전송(대량)

<작업 순서>
1. index 페이지 : 메뉴 선택(radio or select) -> get 방식
2. flask server 파라미터 받기(메뉴 번호)
3. 메뉴 번호 따라서 각 페이지 이동
'''


def db_conn():
    import pymysql
    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor

def select_func() :
    conn, cursor = db_conn()
    cursor.execute("select * from goods")
    data = cursor.fetchall()
    for row in data:
        print('code%d. %s 갯수%d 가격%d' % (row[0], row[1], row[2], row[3]))
    print('전체 레코드 수', len(data))
    cursor.close(); conn.close()
    return data


from flask import Flask, render_template, request

app = Flask(__name__)


# 함수 장식자
@app.route('/') # 기본 url 요청 -> 함수 호출
def index() :
    return render_template('/app04/index.html')


# http://127.0.0.1:5000/select?menu
@app.route('/select', methods=['GET','POST'])
def select() :
    if request.method == 'GET':
        menu = int(request.args.get('menu'))
    if menu == 1: # 레코드 조회
        data = select_func()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)

    if menu == 2: # 레코드 추가
        return render_template("/app04/insert.html")

    if menu == 3: # 레코드 수정
        return render_template("/app04/dudate.html")

    if menu == 4: # 레코드 삭제
        return render_template("/app04/delete.html")



@app.route('/insert2', methods=['GET','POST'])
def insert():
    try:
        if request.method == 'POST' :
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            conn, cursor = db_conn()
            sql = f"insert into goods values({code},'{name}',{su},{dan})"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", error_info=e)

'''
@templates.route('/update2', methods=['GET','POST'])
def update():
    try:
        if request.method == 'POST' :
            code = int(request.form['code'])
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            conn, cursor = db_conn()
            sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e:
        return render_template("/app04/error.html", error_info=e)
'''

@app.route('/delete2', methods=['GET','POST'])
def delete():
    try:
        if request.method == 'POST':
            code = int(request.form['code'])
            conn, cursor = db_conn()
            cursor.execute(f"select*from goods where code={code}")
            row = cursor.fetchone()
            if row:
                cursor.execute(f"delete from goods where code={code}")
            else:
                print('해당 코드 없음')
            conn.commit()
            cursor.close() ; conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e:
        return render_template("/app04/error.html", error_info=e)

@app.route('/dudate2', methods=['GET','POST'])
def dudate():
    try:
        if request.method == 'GET':
           menu = int(request.args.get('menu'))
        if menu == 1:
            return render_template("/app04/dudate2.html")
        if menu == 2:
            return render_template("/app04/dudate3.html")

    except Exception as e:
        return render_template("/app04/error.html", error_info=e)


@app.route('/new2',methods=['GET','POST'])
def new2():
    try:
        if request.method == 'POST' :
            code = int(request.form['code'])
            su = int(request.form['su'])

            conn, cursor = db_conn()
            sql = f"update goods set su = {su} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e:
        return render_template("/app04/error.html", error_info=e)

@app.route('/new3',methods=['GET','POST'])
def new3():
    try:
        if request.method == 'POST' :
            code = int(request.form['code'])
            dan = int(request.form['dan'])

            conn, cursor = db_conn()
            sql = f"update goods set dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)

    except Exception as e:
        return render_template("/app04/error.html", error_info=e)



if __name__ == "__main__":
    app.run()

