'''
원격 서버의 웹 수집
'''

from bs4 import BeautifulSoup # source -> html 파싱
import urllib.request as res # 별칭 : 원격 서버 파일 요청

url = 'http://www.naver.com/index.html' # naver main

# 1. 원격 서버 url 요청
req = res.urlopen(url) # 요청 -> 응답
print(req) # 정상 응답 : object info
data = req.read() # 객체안의 source 가져오기 : read()
print(data) # txt 형식의 source -> 파싱 필요

# 2. source -> html 형식 파싱 (= 특정한 data를 다른 포멧으로 변경하는것)
src = data.decode('utf-8') # decoding -> source
html = BeautifulSoup(src, 'html.parser') # source -> html
print(html) # 문서형식으로 변경 (data 변수와 비교)

# 3. Tag 내용 가져오기
link = html.find('a') # <a href='url'>내용</a>
print(link) # a tag가 최초로 발견된 링크
'''
element : <시작태그 속성명='값'> 화면 내용 </종료태그>
'''
# 태그 내용 추출 : > 내용 </a>
print('a 태그 내용 :', link.string) # a 태그 내용 : 연합뉴스 바로가기

