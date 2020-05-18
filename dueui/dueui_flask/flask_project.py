from flask import Flask, render_template, request

app = Flask(__name__)

# 함수 장식자
@app.route('/') # 기본 url 요청 -> 함수 호출
def index() :
    return render_template('main_map.html')

@app.route('/txt', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        search = request.form['restaurant']
        num = 0
        from bs4 import BeautifulSoup
        import urllib.request as res
        url = f"https://www.google.com/search?q={search}&hl=ko&tbm=nws&ei=kZyiXr_OPN6Mr7wP1YKF8AU&start={num}0&sa=N&ved=0ahUKEwj_2sqMzIDpAhVexosBHVVBAV44ChDy0wMIWw&biw=1553&bih=968&dpr=1"
        req = res.urlopen(url)
        data = req.read()
        src = data.decode('utf-8')
        html = BeautifulSoup(src, 'html.parser')

