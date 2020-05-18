'''
json 파일 2가지 형식

1. 중괄호 : {key:value,...},{key:value,...}
   -> json.loads(row)
2. 대괄호 : [{key:value,...},{key:value,...}]
   -> json.load(row)
'''

import json

# 1번 형식 : 중괄호

# 2번 형식 : 대괄호
file = open('./chap07_File_IO/data/labels.json', encoding = 'utf-8')
# print(file.read())

rows = json.load(file) # json 문자열 -> object
print(len(rows)) # 30
print(rows)

for row in rows[:5] : # [{row},{row}]
    print(row)
    print(type(row))
file. close()

# list -> DataFrame
import pandas as pd
rows_df = pd.DataFrame(rows)
print(rows_df.info())
'''
RangeIndex: 30 entries, 0 to 29
Data columns (total 5 columns):
'''
print(rows_df.head())


# 2. pickle
'''
pytho object(list, dict) -> file(binary) -> python object(list, dict)
'''
import pickle
'''
save : pickle.dump(data, file)
load : pickle.load(file)
'''

# 1) pickle
file = open('./chap07_File_IO/data/rows_data.pickle', mode = 'wb')
pickle.dump(rows, file) # list -> binary
print('pickle file saved')

# 2) pickle load
file = open('./chap07_File_IO/data/rows_data.pickle', mode = 'rb')
rows_data = pickle.load(file)
print(rows_data)
print(type(rows_data))

