'''
텍스트 파일 입출력
형식)
   open(file, mode='r','w','a')
'''

import os # 파일 경로

try :
    print('현재 파일 경로 :', os.getcwd())
    '''
    # file open : 절대 경로
    file = open(os.getcwd() + '/chap07_File_IO/data/ftest.txt', mode = 'r')
    print(file.read()) # file 사용
    file.close()
    '''
    # file open : 상대 경로
    file = open('./chap07_File_IO/data/ftest.txt', mode='r') # . : 현재 경로
    print(file.read())  # file 사용
    file.close()

    # 파일 쓰기
    file2 = open('./chap07_File_IO/data/ftest2.txt', mode='w')
    file2.write('my first text!')
    file2.close()

    # 파일 내용 추가
    file3 = open('./chap07_File_IO/data/ftest2.txt', mode='a')
    file3.write('\nmy second text!')
    file3.close()

    '''
    file.read() : 전체 문서 한번에 읽기
    file.readline() : 전체 문서에서 한 줄 읽기
    file.readLines() : 전체 문서를 줄 단위 읽기
    '''

    # readline // 한줄만 읽어짐
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



