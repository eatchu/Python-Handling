'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 


 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세',
         '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람',
         '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)
spec_str = '[@#$%^&*()]'
punc_str = '[.,;:?!]'

# 1. 소문자 변경 
text2 = [text.lower() for text in texts]

# 2. 숫자 제거
text3 = [sub('\\d','',text) for text in text2]

# 3. 문장부호 제거
text4 = [sub(punc_str,'',text) for text in text3]

# 4. 영문자 제거 
text5 = [sub('[a-z]','',text) for text in text4]

# 5. 특수문자 제거
text6 = [sub(spec_str,'',text) for text in text5]
print(text6)

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)
text7 = [sub('\s{2,}',' ',text) for text in text6]
print(text7)