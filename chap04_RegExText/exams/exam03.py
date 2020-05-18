'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
     사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
    
   <출력 예시> 
유관순 750905-******* 
홍길동 850905-******* 
강감찬 770210-*******  
'''

import re # 정규표현식 패키지 임포트
from re import match, findall, sub

person = """유관순 750905-2049118
홍길동 850905-1059119
강호동 790101-5142142
강감찬 770210-1542001"""

person_list = person.split('\n')
print(person_list)

p = '강감찬 770210-1542001'
r = re.match('[가-힣]{3}\s[0-9]{6}-[1-4]\\d{6}', p)
print(r)
print(findall('[1-4]\\d{6}$',p))
print(sub('[1-4]\\d{6}$','*******',p))



for pp in person_list :
    result = match('[가-힣]{3}\s[0-9]{6}-[1-4]\\d{6}', pp)
    if result :
        print(sub('\\d{7}$','*******',result[0]))


for pp in person_list :
    result = findall('[가-힣]{3}\s[0-9]{6}-[1-4]\\d{6}', pp)
    if result :
         good=result[0]
         good2=good[:11]+('*'*7)
         print(good2)













