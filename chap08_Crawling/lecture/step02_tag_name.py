'''
tag명으로 찾기
형식)
html.find('tag') : 최초로 발견된 tag 1개 수집
html.find_all('tag') : 해당 tag 전체 수집
'''

from bs4 import BeautifulSoup

# 1. local file 불러오기
file = open('./chap08_Crawling/data/html01.html', mode='r', encoding='utf-8')
src = file.read()
print(src)

# 2. src -> html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. tag 찾기 -> 내용 추출

# 1) 계층적 구조로 tag 가져오기
h1 = html.html.body.h1
print(h1) # element : <h1> 시멘틱 태그 ?</h1>
print(h1.string) # 내용 : 시멘틱 태그 ?

# 2) find('tag')로 tag 가져오기
h2 = html.find('h2')
print(h2) # <h2> 주요 시멘틱 태그 </h2>
print(h2.string) # 주요 시멘틱 태그

# 3) find_all('tag')
li = html.find_all('li') # list로 반환
print(li)
print(len(li)) # 5

li_count = [l.string for l in li] # 내용만 꺼내오기
print(li_count)



