'''
tag 속성과 내용 가져오기
 - element : tag + 속성 + 내용
 ex) <a href='www.naver.com'>네이버</a>
a : tag
href : 속성(attribute)
네이버 : 내용(content)
'''

from bs4 import BeautifulSoup

# 1. local file 가져오기
file = open('./chap08_Crawling/data/html02.html', encoding='utf-8')
src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. a 태그 element 가져오기
links = html.find_all('a')
print(links)

# 4. a tag -> attribute(href(5), target(1))
urls = []
for link in links :
    print(link.string) # tag의 내용
    attr = link.attrs
    print(attr)  # tag의 속성 -> key:value 형식으로 반환
    # {'href': 'http://www.duam.net'}
    #print(attr['href']) # http://www.duam.net
    urls.append(attr['href'])
    try :
        print(attr['target']) # error
    except Exception as e :
        print('예외 발생 :', e)
print(urls)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']
print(len(urls)) # 5

# 문제) urls -> 정상 url -> new_urls
from re import findall, match, sub
new_urls = []
for url in urls :
    if url.startswith('http') :
        new_urls.append(url)
print(new_urls)





