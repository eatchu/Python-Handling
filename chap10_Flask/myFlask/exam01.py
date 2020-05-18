'''
문제) emp 테이블을 대상으로 사원명을 조회하는 app을 구현하시오
 조건1> index 페이지에서 사원명을 입력받아서 post 방식 전송
 조건2> 해당 사원이 있으면 result 페이지에 사번, 이름, 직책, 부서번호 칼럼 출력
 조건3> 해당 사원이 없으면 result 페이지에 '해당 사원 없음'을 출력
'''

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('/exam01/index.html')

@app.route('/emp',methods=['GET','POST'])
def search() :
    if request.method == 'POST' :
        name = request.form['name']
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
            sql = "select * from emp"
            cursor.execute(sql)
            data = cursor.fetchall()
            if data :
                sql = f"select eno , ename, job, dno from emp where ename like '%{name}%'"
                cursor.execute(sql)
                data2 = cursor.fetchall()
                ename = str
                data3 = str
                leng = 0
                if data2 :
                    for row in data2:
                        ename = row[1]
                        data3 = f"사원번호 = {row[0]}, 사원이름 = {row[1]}, 직책 = {row[2]}, 부서번호 = {row[3]}"
                    leng = len(data2)

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    return render_template('/exam01/search.html', name=name, data=data3, ename=ename, size = leng)


if __name__ == "__main__":
    app.run()
