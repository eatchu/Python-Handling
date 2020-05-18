'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''

try :
    area = input('지역을 입력하세요 : ')
    file = open('./chap07_File_IO/data/zipcode.txt', mode='r', encoding='utf-8')
    lines = file.readline()
    dong = []

    while lines:
        addr = lines.split(sep='\t')
        if addr[1].startswith(area):
            addr2 = addr[3].split(' ')
            dong.append(addr2[0])
        lines = file.readline()
    unique_dong = set(dong)
    dong2 = list(unique_dong)
    print('서울 특별시 전체 동의 갯수 :', len(dong2),
          '\n', sorted(dong2))

except Exception as e :
    print('예외발생 :', e)
finally :
    file.close()
    
