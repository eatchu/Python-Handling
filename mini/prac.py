import os
import sqlite3
os.getcwd()
os.chdir('C:\\ITWILL\\3_Python\\workspace\\mini')
os.getcwd()

from flask import Flask
from flask import render_template, request

app2 = Flask(__name__)

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
sql = """
create table travel(

city varchar(100) primary key,

 terr int not null, atmp int not null, 

theme int not null, 

season int not null, 

traffic int not null)
"""
cursor.execute(sql)
cursor.execute("insert into travel values('논산 딸기축제', 70, 0, 80, 50, 50);")
cursor.execute("insert into travel values('전주 한옥마을', 50, 25, 60, 50, 50);")
cursor.execute("insert into travel values('부여 궁남지', 50, 10, 100, 20 , 50);")
cursor.execute("insert into travel values('공주 문화유적지', 50, 10, 80, 20 , 50);")
cursor.execute("insert into travel values('천안 천호지와 독립기념관', 30, 10, 90, 30 , 30);")
cursor.execute("insert into travel values('보령 대천 해수욕장', 0, 90, 55, 0 , 50);")
cursor.execute("insert into travel values('아산 온양온천', 80, 0, 100, 80, 40);")
cursor.execute("insert into travel values('군산 선유도', 20, 0, 100, 40, 50);")
cursor.execute("insert into travel values('태안 안면도자연휴양림', 80, 0, 100, 0, 50);")
cursor.execute("insert into travel values('서산 웅도갯벌', 0, 30, 80, 60, 50);")
cursor.execute("insert into travel values('인천 월미도', 0, 70, 55, 0, 30);")
cursor.execute("insert into travel values('독도와 울릉도', 0, 0, 80, 30, 100)")
cursor.execute("insert into travel values('흑산도', 0, 0, 100, 100, 100)")
cursor.execute("insert into travel values('청산도', 100, 0, 100, 100, 90)")
cursor.execute("insert into travel values('강릉(바다열차)', 0,50 ,100 ,100 , 80)")
cursor.execute("insert into travel values('양양(서피비치)',0 , 80,25 ,0 , 80)")
cursor.execute("insert into travel values('평창(대관령 양 떼 목장)',90 , 20, 55, 40, 80)")
cursor.execute("insert into travel values('화천(산천어 축제)',20 ,70 ,80 ,100 ,80 )")
cursor.execute("insert into travel values('속초(중앙시장)',50 , 80, 70, 40, 80)")
cursor.execute("insert into travel values('흥천(비발디 파크 스키장)',80 ,80 ,30 ,100 ,80 )")
cursor.execute("insert into travel values('정선(강원랜드)', 50,100 , 0,40 , 80)")
cursor.execute("insert into travel values('인제(자작나무 숲)',90 ,30 , 100, 30, 80)")
cursor.execute("insert into travel values('춘천(김유정역)', 70,50 ,80 , 40, 80)")
cursor.execute("insert into travel values('고창(고인돌 유적지)', 70,30 , 80,40 ,80 )")
cursor.execute("insert into travel values('담양(죽녹원)', 80, 30,100 , 40, 80)")
cursor.execute("insert into travel values('전주(전주 한옥마을)', 60, 70, 55,40 ,80 )")
cursor.execute("insert into travel values('제주(협재해수욕장)', 0,70 , 40, 0,100 )")
cursor.execute("insert into travel values('제주(성산일출봉)', 70, 50,90 ,30 ,100 )")
cursor.execute("insert into travel values('제주(사려니숲길)',90 , 30, 100,30 ,100 )")
cursor.execute("insert into travel values('제주(동문시장)',50 ,70 , 70,40 , 100)")
cursor.execute("insert into travel values('제주(해녀체험)', 20, 30, 80,40 , 100)")
cursor.execute("insert into travel values('제주(카페 및 소품샵 투어)',50 , 50,55 ,40 ,100 )")
cursor.execute("insert into travel values('서울 롯데월드',  50,  90,  25,  50,  0 )")
cursor.execute("insert into travel values('서울 국립현대미술관', 50,  25,  80,  50,  0)")
cursor.execute("insert into travel values('서울 벽화마을',  50,  70,  65,  50,  0)")
cursor.execute("insert into travel values('서울 코엑스',  50,  75,  35,  50,  0)")
cursor.execute("insert into travel values(' 서울 창덕궁',  50,  65,  80,  50,  0)")
cursor.execute("insert into travel values(' 과천 서울랜드', 50,  80,  25,  50,  20)")
cursor.execute("insert into travel values(' 대부도 아쿠아시티',  20,  50,  25,  0,  30)")
cursor.execute("insert into travel values('양평 유명산 패러글라이딩', 100,  50,  25,  50,  40)")
cursor.execute("insert into travel values(' 가평 수상레저',  80,  70,  25,  0,  30)")
cursor.execute("insert into travel values(' 고양 아쿠아플라넷',  50,  60,  25,  0,  20)")
cursor.execute("insert into travel values(' 경북 영덕 대게 축제', 10, 70, 75, 100, 70)")
cursor.execute("insert into travel values(' 경북 경주 안압지', 75, 10, 95, 50, 70)")
cursor.execute("insert into travel values(' 경남 태화강 십리대 숲', 85, 10, 100, 30, 80)")
cursor.execute("insert into travel values('경남 통영 미륵산', 100, 10, 100,50, 70)")
cursor.execute("insert into travel values(' 경북 안동 하회마을', 85, 20,100, 50, 70)")
cursor.execute("insert into travel values(' 경북 문경시 문경새재', 85, 10,100, 55, 65)")
cursor.execute("insert into travel values(' 경남 감천문화마을', 60, 70,55, 50, 85)")
cursor.execute("insert into travel values(' 경남 백두산천지 온천', 85, 30, 100, 70, 65)")
cursor.execute("insert into travel values(' 대구 방천시장', 50, 70, 65, 50, 70)")
