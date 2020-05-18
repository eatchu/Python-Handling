'''
선택자(selector)
 - 웹 문서 디자인(css)에서 사용
 - 선택자 : id(#), class(.)
 - html.select('선택자') : 여러개 element 수집
 - html.select_one('선택자') : 해당하는 1개의 element 수집
'''

from bs4 import BeautifulSoup

file = open('./chap08_Crawling/data/html03.html', encoding = 'utf-8')
src = file.read()
print(src)

html = BeautifulSoup(src, 'html.parser')
print(html)


# 1) id 선택자
table = html.select_one('#tab')
print(table)

# <table> <tr> <th> or <td>
ths = html.select('#tab > tr >th') # list
print(ths)
print(len(ths)) # 4

for th in ths :
    print(th.string) # tag 내용

# 2) class 선택자
trs = html.select('#tab > .odd') # 5<tr> -> 2<tr>
print(trs)

for tr in trs :
    tds = tr.find_all('td')
    for td in tds :
        print(td.string)


# 3) tag[속성='값'] 찾기
trs = html.select("tr[class='odd']")
print(trs)
for tr in trs :
    tds = tr.find_all('td')
    for td in tds :
        print(td.string)
