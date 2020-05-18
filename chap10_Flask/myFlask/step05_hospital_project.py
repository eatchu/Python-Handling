
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


from flask import Flask, render_template, request

app = Flask(__name__)

# 함수 장식자
@app.route('/') # 기본 url 요청 -> 함수 호출
def index() :
    return render_template('/app05/main.html')

@app.route('/docForm')
def docForm():
    return render_template('/app05/docForm.html')

@app.route('/nurseForm')
def nurseForm():
    return render_template('/app05/nurseForm.html')


@app.route('/docPro', methods=['GET','POST'])
def docPro():
    if request.method == 'POST':
        doc_id = int(request.form['id'])
        major = request.form['major']

        conn,cursor=db_conn()
        sql = f"""select * from doctors where doc_id={doc_id}
               and major_treat='{major}'"""
        cursor.execute(sql)
        row = cursor.fetchone()
        if row: #login 성공
            # print('login 성공')
            sql = f"""select d.doc_id, t.pat_id, t.treat_contents, t.tread_date
                  from doctors d inner join treatments t 
                  on d.doc_id = t.doc_id and d.doc_id = {doc_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()

            if data :
                for row in data :
                    print(row)

                size = len(data)
            else :
                size = 0
        else: #login 실패
            return render_template('/app05/error.html', info="id 또는 진료과목 확인")

        return render_template('/app05/docPro.html', dataset=data, size=size)


@app.route('/docPro2/<nu>')
def docPro2(nu):
        conn,cursor=db_conn()
        sql = f"""select * from doctors where doc_id={nu}"""
        cursor.execute(sql)
        row = cursor.fetchone()
        if row: #login 성공
            # print('login 성공')
            sql = f"""select d.doc_id, t.pat_id, t.treat_contents, t.tread_date
                  from doctors d inner join treatments t 
                  on d.doc_id = t.doc_id and d.doc_id = {nu}"""
            cursor.execute(sql)
            data = cursor.fetchall()

            if data :
                for row in data :
                    print(row)

                size = len(data)
            else :
                size = 0
        else: #login 실패
            return render_template('/app05/error.html', info="id 또는 진료과목 확인")

        return render_template('/app05/docPro.html', dataset=data, size=size)



@app.route('/nursePro', methods=['GET','POST'])
def nursePro():
    if request.method == 'POST':
        nur_id = int(request.form['id'])
        conn,cursor=db_conn()
        sql = f"""select * from nurses where nur_id={nur_id}"""
        cursor.execute(sql)
        row = cursor.fetchone()
        if row: #login 성공
            # print('login 성공')
            sql = f"""select nur_name, doc_id, pat_name, pat_phone 
                  from nurses n inner join patients p
                  on n.nur_id=p.nur_id and n.nur_id={nur_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            if data :
                for row in data :
                    print(row)
                size = len(data)
            else :
                size = 0

        else: #login 실패
            return render_template('/app05/error.html', info="id 또는 진료과목 확인")

        return render_template('/app05/nursePro.html', dataset=data, size=size)


@app.route('/patPro/<num>')
def patPro(num):
    conn, cursor = db_conn()
    sql = f"""select pat_name, pat_gen, pat_jumin, pat_addr, pat_phone, pat_email, pat_job
           from patients where pat_id = {num}"""
    cursor.execute(sql)
    data = cursor.fetchone()

    return render_template('/app05/patPro.html', data=data)


if __name__ == "__main__":
    app.run()



