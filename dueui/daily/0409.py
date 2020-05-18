# 문자열 찾기 (R의 stringr 패키지와 유사)

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# 숫자 찾기
findall('[0-9]', st1)
findall('\d',st1)


# r의 역할
'''
역슬래시(\)를 문자열로 인식하게 해주는 함수
'''

# 정수를 입력받아서 제곱한 값을 반환하는 함수를 만들어보자.
def double(x) :
    return x**2
x = double(3)
print(x)

# 각 chapter 별 step 통합해서 파일 하나로 묶기 -> 내가 보기 편하게
# 손에 잘 안익는 함수 다시 익히기
# 오늘 ppt 파일 정독하고 다 사용해보기


















