'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_warp" 선택자  > form > table 태그 내용 출력 
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력  
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기 
file = open('./chap08_Crawling/data/login.html', encoding='utf-8')
fr = file.read()

# 2. html 파싱
html = BeautifulSoup(fr,'html.parser')
print(html)

# 3. 선택자 이용 태그 내용 가져오기
# 조건 1
div = html.select_one('#login_wrap')
print(div)
# 조건 2
table = html.select_one('#login_wrap > form > table')
# table = html.select_one('#login_wrap > form > #login_t')
print(table)
# 조건 3
trs = html.find_all('tr')
print(trs)
for tr in trs :
    ths = tr.find_all('th')
    for th in ths :
        print(th.string)


