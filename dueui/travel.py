
from flask import Flask, render_template ,request # templates 생성, html 템플릿 호출

app = Flask(__name__) # object -> templates object

# 함수 장식자
@app.route('/') # 기본 url 요청 -> 함수 호출
def index() :
    return render_template('index.html')

@app.route('/trav', methods=['GET','POST'])
def trav():
    if request.method == 'GET':
        terr = int(request.args.get('terr'))
        atmp = int(request.args.get('atmp'))
        theme = int(request.args.get('theme'))
        season = int(request.args.get('season'))
        traffic = int(request.args.get('traffic'))
    user = [terr,atmp,theme,season,traffic] # 사용자가 입력한 값 리스트에 저장
    data = select_func() # 데이터베이스에서 데이터 호출
    tot = [] # 결과값을 넣을 리스트
    for row in data:
        a = (row[1]-user[0])**2 + (row[2] - user[1])**2 + \
            (row[3] - user[2])**2 + (row[4] - user[3])*2 + (row[5] - user[4])**2
        tot.append(a)
    min_city = data[tot.index(min(tot))] # 최솟값을 가진 도시를 변수에 저장





if __name__ == "__main__":
    app.run()





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
    cursor.execute("select * from travel")
    data = cursor.fetchall()
    print('전체 레코드 수', len(data))
    cursor.close(); conn.close()
    return data


data = select_func()
print(data)
print(len(data))
for i in data:
    print(i)

user = [0,0,25,60,50]
tot = []
for row in data:
    a = (row[1]-user[0])**2 + (row[2] - user[1])**2 + (row[3] - user[2])**2 + (row[4] - user[3])*2 + (row[5] - user[4])**2
    tot.append(a)
city = data[tot.index(min(tot))]
photo_index = tot.index(min(tot))


