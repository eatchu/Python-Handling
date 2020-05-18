'''
csv, excel file read/write
 - 칼럼 단위로 작성된 파일 유형

cmd에서 외부 라이브러리 설치
 pip install pandas
'''

import pandas as pd # 별칭 생성
import os
print(os.getcwd())

# 1. csv file read
spam_data = pd.read_csv('./chap07_File_IO/data/spam_data.csv',header=None,encoding='ms949')
print(spam_data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns): 칼럼(0,1)
'''
print(spam_data)

# 1) x,y 변수 선택
target = spam_data[0] # DF[칼럼]
texts = spam_data[1] # DF[칼럼]
print(target) # index + data 같이 출력
print(texts)


# 2) target -> dummy
target = [1 if x == 'spam' else 0 for x in target]
print(target) # [0, 1, 0, 1, 0]


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

    # 5. 영문자 제거
    texts_re5 = [sub('[a-z]', '', text) for text in texts_re4]

    # 5. 공백 제거
    texts_re6 = [' '.join(text.split()) for text in texts_re5]
    return texts_re6


clean_txt = clean_text(texts)
print('텍스트 전처리 후')
print(clean_text)

#######################
# bmi.csv
#######################
bmi = pd.read_csv('./chap07_File_IO/data/bmi.csv',encoding='ms949')
print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20001 entries, 0 to 20000
Data columns (total 3 columns):
'''
print(bmi.head()) # 앞부분 5개
print(bmi.tail()) # 뒷부분 5개

height = bmi['height']
weight = bmi['weight']
label = bmi.label

print(len(height)) # 20000
print(len(label)) # 20000

print('키 평균 :', height.mean())
print('몸무게 평균 :', weight.mean())
# 키 평균 : 164.9379
# 몸무게 평균 : 62.40995

# max / min
print('가장 키가 큰 사람 : ',max(height)) # 190
print('가장 몸무게가 많이 나가는 사람 : ',max(weight)) # 85

# 정규화
height_nor = height/max(height)
weight_nor = weight/max(weight)

print(height_nor.mean()) # 0.8680942105263159
print(weight_nor.mean()) # 0.734234705882353

# 범주형 변수 : label
label.value_counts() # 빈도수
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''

# 2. excel file read
'''
pip install xlrd
'''

excel = pd.ExcelFile('./chap07_File_IO/data/sam_kospi.xlsx')
print(excel)

kospi = excel.parse('sam_kospi')
print(kospi)
print(kospi.info())


# 3. csv file save
# 파생변수 생성
kospi['Diff'] = kospi.High - kospi.Low
print(kospi.info()) # 칼럼 추가된거 확인

# csv file 저장
kospi.to_csv('./chap07_File_IO/data/kospi_df.csv', index=None, encoding='utf-8')
# 저장한 파일 확인
kospi_df = pd.read_csv('./chap07_File_IO/data/kospi_df.csv', encoding='utf-8')
print(kospi_df.head())