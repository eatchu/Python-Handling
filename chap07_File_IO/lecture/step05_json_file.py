'''
JSON 파일
 - 네트워크에서 표준으로 사용되는 파일 형식
 - 파일 형식 : {key:value, key:value...}, {key:value, key:value...}...
 - 활용 예 : 서로 다른 플랫폼(java, python)에서 파일 공유

 - JSON 모듈
 1. encoding : file save : python object (list, dict) -> json file
 2. decoding : file read : json file -> python object
'''

import json

# 1. encoding
'''
python object -> json 문자열
형식) json.dumps(object)
'''

# python object 생성
user = {'id':1234, 'name':'홍길동'}
print(type(user)) # <class 'dict'>
# json 문자열 생성 : json.dumps(object)
json_str = json.dumps(user, ensure_ascii=False) # unicode -> ascii 변경 x
print(json_str) # {'id':1234, 'name':'홍길동'}
print(type(json_str)) # <class 'str'>


# 2. decoding :
'''
json 문자열 -> python object
형식) json.loads(json 문자열)
'''

py_obj = json.loads(json_str)
print(py_obj) # {'id': 1234, 'name': '홍길동'}
print(type(py_obj)) # <class 'dict'>

# 3. json file read/write

# 1) json file read : decoding
import os
file = open('./chap07_File_IO/data/usagov_bitly.txt', encoding = 'utf-8')
data = file.readlines()
file.close()
print(data)

# decoding하기 : json 문자열 -> python object
rows = [json.loads(row) for row in data]
print(len(rows)) # 3560

for row in rows[:10] :
    print(row)
    print(type(row)) # <class 'dict'>

# json object -> Dataframe
import pandas as pd
rows_df = pd.DataFrame(rows)
print(rows_df.info())
print(rows_df.head())
print(rows_df.tail())


# 2) json file write : json encoding
file = open('./chap07_File_IO/data/usagov_bitly.txt', mode='w', encoding = 'utf-8')
print(type(rows)) # <class 'list'>

for row in rows[:100] :
    json_str = json.dumps(row)
    file.write(json_str)
    file.write('\n')
print('file 저장 완료')

# 3) json file read : json decoding
file = open('./chap07_File_IO/data/usagov_bitly.txt', encoding = 'utf-8')
data = file.readlines()
print(len(data))

# json decoding
rows = [json.loads(row) for row in data] # json 문자열 -> python object
rows_df = pd.DataFrame(rows)
print(rows_df.info()) # 100 line만 꺼냄


