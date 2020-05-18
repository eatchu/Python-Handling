'''
사용자 정의 함수 응용
'''

# 1. 텍스트 전처리 용도 함수
def clean_text(texts) :
    from re import sub
    # 1. 소문자 변경
    texts_re = [text.lower() for text in texts]

    # 2. 슷자 제거
    texts_re2 = [sub('\\d', '', text) for text in texts_re]

    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = [sub(punc_str, '', text) for text in texts_re2]

    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = [sub(spec_str, '', text) for text in texts_re3]

    # 5. 공백 제거
    texts_re5 = [sub('\s', ' ', text) for text in texts_re4]
    return texts_re5

texts = [' 우리나라    대한민국, 우리나라%$ 만세',
         '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람',
         '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
print('텍스트 전처리 전')
print(texts)
print('텍스트 전처리 후')
clean_text(texts)


def clean_text2(texts) :
    from re import sub
    # 1. 소문자 변경
    texts_re = texts.lower()

    # 2. 슷자 제거
    texts_re2 = sub('\\d', '', texts_re)

    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = sub(punc_str, '', texts_re2)

    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = sub(spec_str, '', texts_re3)

    # 5. 공백 제거
    texts_re5 = sub('\s{2,}', ' ',texts_re4)
    return texts_re5

texts2 = [clean_text2(text) for text in texts]
print(texts2)




# 2. 표본의 분산과 표준편차
from statistics  import mean, variance, stdev
from math import sqrt
dataset = [2,4,5,6,1,8]
print(mean(dataset)) # 평균
print(variance(dataset)) # 분산
print(stdev(dataset)) # 표준편차

'''
분산 = sum(x변량-평균)**2/(n-1)
표준편차 = sqrt(분산)
 - sqrt(루트) 제공 모듈은 math
'''


def var_std (dataset) :
    from statistics import mean
    from math import sqrt
    avg = mean(dataset)
    diff = [(x-avg)**2 for x in dataset]
    diff_sum = sum(diff)
    var = diff_sum/(len(dataset)-1)
    std = sqrt(var)
    return var, std

x, y = var_std(dataset)
print(x,y)


