'''
step01 try 예외처리
'''

# 유형별 오류 처리
print('유형별 예외처리')
try :
    div = 1000 / 2.5 # 정상
    print('div = %.3f'%(div))
    num = int(input('숫자입력'))
    print('num=',num)
except ZeroDivisionError as e:  # class as object
    '''
    이런 식의 오류 코드를 작성했을때 발생하는 예외 처리
    div2 = 1000 / 0 # 산술적 예외
    print('div2 = %.3f'%(div2))
    '''
    print('예외발생 : ', e)  # 예외발생 :  division by zero
except FileNotFoundError as e:  # File IO 예외처리
    '''
    잘못된 파일명이나 위치를 입력했을때 발생하는 예외처리
    '''
    print('예외발생 : ', e)  # [Errno 2] No such file or directory: 'c:/text.txt'
except Exception as e:  # 나머지 예외처리
    print('기타 예외발생 : ', e)
finally:
    print('프로그램 종료')

'''
step02 text file
'''

try :
    # 1. file open : 경로 설정 후 파일 꺼내기
    file = open('./chap07_File_IO/data/ftest.txt', mode='r') # . : 현재 경로
    print(file.read())  # file 사용
    file.close()

    # 2. 파일 쓰기 : mode = w, file.write()
    file2 = open('./chap07_File_IO/data/practice1.txt', mode='w')
    file2.write('my first text! \n this is my practice \n it\'s so hard to learn python')
    file2.close()

    # 파일 내용 추가 :  mode = a
    file3 = open('./chap07_File_IO/data/practice1.txt', mode='a')
    file3.write('\nmy second text!')
    file3.close()

    # readline : 한줄만 읽어짐
    file4 = open('./chap07_File_IO/data/ftest2.txt')
    # row = file4.readline()
    for i in range(2) :
        row = file4.readline()
        print('row :' + str(i+1) ,row)
    print(row)
    file4.close()

    # readlines() : 전체 문장을 줄단위 읽기
    file5 = open('./chap07_File_IO/data/ftest2.txt')
    rows = file5.readlines()
    print(rows) # ['my first text!\n', 'my second text!']
    for row in rows :
        for sent in row.split('\n') :
            if sent :
                print(sent)

    # string.strip() : 문장 끝 불용어(공백, \n\t 기타) 제거
    print('strip 함수')
    for row in rows :
        print(row.strip())

    str_text = 'agsgs234\n \t\r'
    print('str_text :', str_text.strip()) # str_text : agsgs234
    file5.close()

    # with
    # file.close()를 사용할 필요 없음. 구문이 끝나면 객체가 자동으로 사라짐
    with open('./chap07_File_IO/data/ftest3.txt', 'w', encoding = 'utf-8') as file6 : # 쓰기용 파일 객체
        file6.write('파이썬 파일 작성 연습')
        file6.write('\n 파이썬 파일 작성 연습2')
    with open('./chap07_File_IO/data/ftest3.txt', 'r', encoding = 'utf-8') as file7 : # 읽기용 파일 객체
        print(file7.read())

except FileNotFoundError as e :
    print('예외 정보 : ', e)

finally :
    pass

'''
step03 우편번호 검색
'''

try :
    dong = input('동을 입력하세요 :')
    file = open('./chap07_File_IO/data/zipcode.txt','r',encoding = 'utf-8')
    line = file.readline()

    while line : # null == False 주소가 있는데로 while문 반복
        addr = line.split(sep='\t')
        if addr[3].startswith(dong) :
            print('['+addr[0]+']',addr[1],addr[2],addr[3],addr[4])

        line = file.readline() # 두번째 줄 주소 읽음

    # print(line) # ﻿135-806	서울	강남구	개포1동 경남아파트		1
    # print(line.split('\t')) # ['\ufeff135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']

except Exception as e :
    print('예외 발생 :', e)
finally :
    file.close()
    print('종료')

'''
step04 csv, excel file
'''

import pandas as pd
from pandas import read_csv

# 1. csv file read : spam_data.csv
spam_data = read_csv('./chap07_File_IO/data/spam_data.csv',header=None,encoding='ms949')
print(spam_data.info())
'''
spam_data : 데이터 프레임
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns): 칼럼(0,1)
'''
print(spam_data)

# 1) x,y 변수 선택 : DF[칼럼]
target = spam_data[0] ; texts = spam_data[1]
print(target)
print(texts)

# 2) target -> dummy
target = [1 if x == 'spam' else 0 for x in target]
print(target) # [0, 1, 0, 1, 0]

# 3) text 전처리
from chap07_File_IO.lecture.step04_csv_excel import cleantext
clean_txt = clean_text(texts)
print(clean_txt)


# 2. csv file read 2 : bmi.csv

bmi = read_csv('./chap07_File_IO/data/bmi.csv', encoding='ms949') # 칼럼명(head) 존재
print(bmi.info())
'''
dataframe , 20000 row, 3 columns
'''
print(bmi.head()) # 앞부분 5개
print(bmi.tail()) # 뒷부분 5개

# 칼럼단위로 꺼내는 방식
# 형식1) df['column'], 형식2) df.column
height = bmi['height']
weight = bmi.weight
label = bmi.label

print(len(height)) # 20000

# pandas 패키지에 자체적으로 가지고 있는 함수 : math 패키지 호출 필요 없음
print('키 평균 :', height.mean()) # 키 평균 : 164.9379
print('몸무게 평균 :', weight.mean()) # 몸무게 평균 : 62.40995

# max / min
print('가장 키가 큰 사람 : ',max(height)) # 190
print('가장 몸무게가 많이 나가는 사람 : ',weight.max()) # 85

# 정규화 : 각 값에 가장 큰 값으로 나누어주어 모든 값의 범위를 0~1로 만들어줌
height_nor = height/max(height)
weight_nor = weight/max(weight)

print(height_nor.mean()) # 0.8680942105263159
print(weight_nor.mean()) # 0.734234705882353

# 범주형 변수 : label
label.value_counts() # 빈도수 확인하기
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''

# 3. excel file read : sam_kospi.xlsx
# xlrd 패키지 설치 필요
import pandas as pd
excel = pd.ExcelFile('./chap07_File_IO/data/sam_kospi.xlsx')
print(excel) # 안읽혀짐 -> 파싱해줘야함
# 파싱하기
kospi = excel.parse('sam_kospi')
print(kospi)
print(kospi.info()) # 246 x 6

# 4. csv file save
# 파생변수 생성
kospi['Diff'] = kospi['High'] - kospi['Low']
kospi['Diff'] = kospi.High - kospi.Low
print(kospi.info()) # 칼럼 추가된거 확인

# csv 저장
kospi.to_csv('./chap07_File_IO/data/kospi_df.csv', index=None, encoding='utf-8')

# 저장한 파일 확인
kospi_df = pd.read_csv('./chap07_File_IO/data/kospi_df.csv', encoding='utf-8')
print(kospi_df.head())

'''
step05 json
'''

'''
step06 pickle
'''

