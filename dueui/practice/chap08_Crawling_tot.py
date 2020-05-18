'''
step01 url request
 - url encoding 형식 확인하는 법 : 페이지소스보기 -> charset 확인
'''

# url request - package : urllib.request.urlopen
from urllib.request import urlopen

url = 'http://www.naver.com/index.html'

# 1. 함수 사용해서 url 요청하기
file = urlopen(url)
print(file) # <http.client.HTTPResponse object at 0x000001752F7E5688>

# 2. 꺼내온 url source 만들기
file2 = file.read()
print(file2) # list 형태로 반환됨 : b'<!doctype html>\n\n\n\content="origin">\n<meta http-equiv="Content-Script-Type" ...

# 3. encoding 바꿔주기
src = file2.decode('utf-8') # or 'cp949'
print(src) # <strong class="bl_t">제주 감귤빵을 집에서?</strong> ...

# 4. parsing 해주기
# 패키지 설치 : BeautifulSoup
from bs4 import BeautifulSoup
html = BeautifulSoup(src,'html.parser')
print(html)


'''
step02 tag 가져오기
'''

# url이 아닌 파일을 꺼내올때
file = open('./chap08_Crawling/data/html01.html', mode='r', encoding='utf-8')
src = file.read()
html = BeautifulSoup(src,'html.parser')
print(html)

# 계층적 구조로 tag 찾기
h1 = html.html.body.ul
print(h1) # <ul> 하위의 내용 출력 </ul>

# 함수 사용 find_all('tag') 찾기 : list 형태로 반환
h2 = html.find('ul')
print(h2) # <ul> 하위의 내용 출력 </ul>

h3 = html.find_all('li')
print(h3)
str = [i.string for i in h3]
print(str)

'''
step03 tag 속성
'''
from bs4 import BeautifulSoup
file = open('./chap08_Crawling/data/html02.html',encoding='utf-8')
src = file.read()
html = BeautifulSoup(src,'html.parser')
data = html.find_all('a')
urls = []
for row in data :
    print(row.attrs)  # tag의 속성 -> key:value 형식으로 반환
    urls.append(row.attrs['href']) # 'href'키의 value : domain
print(urls)

new_urls = [i for i in urls if i.startswith('http')]
print(new_urls)

'''
step04 selector 선택자 : id(#), class(.)
'''

file = open('./chap08_Crawling/data/html03.html', encoding = 'utf-8')
src = file.read()
html = BeautifulSoup(src, 'html.parser')
print(html)


