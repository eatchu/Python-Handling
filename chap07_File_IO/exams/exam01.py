#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 

'''
문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문단 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

import os
os.getcwd()
file = open('./chap07_File_IO/data/ftest.txt', mode = 'r')
cnt = 0
txt = []
for row in file.readlines() :
    for sent in row.split('\n') :
        if sent :
            txt.append(sent)
    cnt += 1
print(txt)
print('문단 수 : %d'%(cnt))


word = []
cnt2 = 2
for t in txt :
    for s in t.split(' '):
        if s :
           word.append(s)
           cnt2 += 1
print(word)
print('단어 수 :', cnt2)
