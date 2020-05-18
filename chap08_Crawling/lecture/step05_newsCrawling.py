'''
1. news Crawling
   url : http://media.daum.net
2. pickle save
   binary file save
'''

import urllib.request as res # url 요청 패키지
from bs4 import BeautifulSoup # html 파싱

url = 'http://media.daum.net'

# 1. url 요청
req = res.urlopen(url)
src = req.read() # source로 읽어오기
print(src)
# 2. html 파싱
data = src.decode('utf-8')
print(data)
html = BeautifulSoup(data,'html.parser')
print(html)

# 3. 뉴스기사 : tag[속성='값'] -> 'a[class="link_txt"]'
links = html.select('a[class="link_txt"]')
print(len(links)) # 62개 기사
print(links)

# 내용 꺼내기
crawling_data = [] # list
for link in links :
    link_str = str(link.string) # 내용 추출
    crawling_data.append(link_str.strip()) # 문장 끝에 불용어 처리
print(crawling_data) # list type


# 4. picklie file save
import pickle

# save
file = open('./chap08_Crawling/data/new_crawling.pickle', mode='wb')
pickle.dump(crawling_data, file)
print('pickle file saved')

