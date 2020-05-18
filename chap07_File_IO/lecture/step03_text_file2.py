'''
우편번호 검색
[우편번호]tab[도/시]tab[구]tab[동]
135-886 서울 강남구 개포1동 강남아파트
[우편번호]tab[도/시]tab[구]tab[동]tab[세부주소]
135-886 서울 강남구 개포1동 우성3차아파트 (1-6동) 2
'''

import os
print(os.getcwd())

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