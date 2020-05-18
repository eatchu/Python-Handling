import os
import sqlite3
os.getcwd()
os.chdir('C:\\IITT\\3_Python-I\\workspace\\mini')
os.getcwd()

from flask import Flask
from flask import render_template, request

app2 = Flask(__name__)


def KNNcal(location, atmosphere, theme, season, distance, data):
    userInfo = [location, atmosphere, theme, season, distance]
    result = []
    city = ""
    for row in data:
        num = 0
        for i in range(1, len(row)):
            k = (row[i] - userInfo[i - 1]) ** 2
            num = num + k
        result.append(num)
    idx = result.index(min(result))
    city = data[result.index(min(result))][0]
    return city, idx


comment = ["달려라,바다열차! 기차타고 즐기는 강릉~동해~삼척 해안선 여행","내생에 한번쯤, 서핑에 반할지도! 망망대해를 바로보고 서핑하는 묘미","드넓은 초원, 첩첩산과 전원풍경이 펼쳐지는 이국적인 대관령 양떼목장",
           "'물 반 고기 반'이라고 전해~라, 최고의 축제, 화천 산천어축제","닭강정골목, 속초항 양미리와 도루묵 다양한 먹을거리가 있는 속초 중앙시장","땅도 숲도 하늘도 온통 하얀 세상 속에 우뚝 서 있는 자작나무는 얼마나 황홀할까",
           "스키 or 보드 당신의 선택은? 복합리조트, 비발디파크","룰렛, 블랙잭, 슬롯머신 각종 게임을 즐길 수 있는 이곳은 파라다이스","전철 타고 떠나는 이야기 마을, 춘천 김유정문학촌","세계 최대 고인돌 왕국에 가다, 고창 고인돌 유적",
           "초록 담은 담양을 걸어보세요. 대나무숲 죽녹원","한복 입고 걷고, 춤추고, 노래하고, 맛보는 슬로우 시티 전주","이 여름 어느바다로 뛰어들까? 제주에서 손꼽히는 해수욕장인 협재해수욕장","유네스코 세계자연유산. 아름다운 화산체, 성산일출봉",
           "치유의 숲, 피톤치드 뿜뿜, 꿈결같은 산책, 사려니 숲길","제주의 전통재래시장 동문시장에서 제주를 맛보다","유네스코 인류무형문화유산 해녀, 나도 제주 해녀가 되고 싶어요","제주 감성 넘치는 카페에서 커피한잔 마시고, 소품샵에서 또다른 제주를 느끼다. ",
           "날씨와 관계없이 1년 365일, 매일 짜릿한 스릴이 넘쳐나는 모험과 신비의 나라 롯데월드!","비슬나무 그늘 아래 예술의 섬, 국립현대미술관 서울관","아날로그 갬성~ 듬뿍 '이화동 벽화마을&낙산성곽길' 나들이","아시아 최대의 지하 쇼핑몰 코엑스는 만남의 장소에요",
           "작은 문과 함께 건물들이 아기자기하게 모여있는 궁","서울대공원은 세계 각국의 야생동물들이 살아 숨 쉬는 서울동물원과 다양한 재미와 즐거움을 주는 서울랜드 ","물빛 그윽한 풍경에 짜릿한 수상 스포츠까지",
           "하늘에서 내려다 보는 새로운 세상", "대부도에서 바다의 매력에 빠져보자!", "청량한 물소리와 하늘 빛, 자연을 한 눈에 품은 감각있는 사람들의 오감만족", "영덕 천년사랑 왕의 대게가 있는 곳",
           "한밤에 더욱 찬란하게 빛나는 신라 역사", "도심 한복판에서 만나는 초록 세상", "미륵산을 비행하는 10분의 행복 한번으론 멈출 수 없는 짜릿함, 통영루지 통영에서 맛보는 별의별 굴 요리", "우리의 아름다운 전통문화의 자긍심을 찾다, 안동 하회마을",
           "문경새재를 따라 기쁜 소식을 들어볼까?", "부산의 과거와 현재가 만나는 곳", "몸과 마음이 따뜻해지는 가조 온천", "대구 방천시장, 예술로 탈바꿈하다", "벚꽃 잔치의 최고봉 봄날의 낭만에 취하다.",
           "50여 년의 재배역사를 자랑하는 논산시의 대표적 지역 특산물로 다양한 프로그램을 체험하고 싶다면~?", "볼거리, 즐길거리, 체험거리가 가득한 한국적 정취 가득한, 전주 한옥마을! 도심 속에서 바라보는 한옥의 아름다움",
           "선화공주와 무왕의 사랑이 담겨있는 인공 연못과 연꽃이 만발하는 곳.", "백제의 옛수도에서 역사의 숨결을 느낄 수 있는곳.", "같이 호수를 한바퀴 걸으면 연인이 된다는 천호지, 그리고 빼놓을 수 없는 천안 명소 독립기념관",
           "휴식과 힐링이 만나는곳. 상쾌함과 시원함이 있는 휴가 여행지!", "겨울 추위를 녹이는 온기, 피부로 먹는 보약 '온천'을 즐겨보자", "신선을 만나는곳 선유도, 타임머신을 타고 돌아간것 같은 시간이 멈춰선곳 군산",
           "탐방로 따라 걸으며 만나는 야생화와 감미로운 자연 속 휴식처를 찾는다면?", "바다 위를 걸어 광활한 갯벌과 서해바다를 굽어보자!", "인천 도심을 즐기자. 월미도 테마파크와 바닷가를 함께 즐길 수 있는곳!",
           "섬들이 노는 섬, 섬을 기억하는 시간", "한반도 서남단 깊고 검은 섬, 흑산도 홍어와 함께하는 겨울 바다", "더딘 풍경으로 삶의 쉼표가 되는 섬, 슬로시티 청산도에서 여유를 즐기는건 어떨까요?", "새가 입에 먹이를 물고 잠시 쉬어가는 아름다운 쉼표 관매도"
           ]


@app2.route('/')
def Index():
    return render_template('index.html')

@app2.route('/subform1', methods = ['GET', 'POST'])
def subform():
    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
        return render_template('purposeform.html', name = name)
@app2.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        conn = sqlite3.connect('sqlite.db')
        cursor = conn.cursor()
        cursor.execute("select * from travel")
        data = cursor.fetchall()
        theme = int(request.args.get('purpose'))
        location = int(request.args.get('location'))
        distance = int(request.args.get('distance'))
        season = int(request.args.get('season'))
        atmosphere = int(request.args.get('atmosphere'))
        city, idx = KNNcal(location, atmosphere, theme, season, distance, data)
        comm = comment[idx]
        return render_template('result.html', city = city, idx = idx, com = comm)


if __name__== "__main__":
    app2.run(host="192.168.12.6")




