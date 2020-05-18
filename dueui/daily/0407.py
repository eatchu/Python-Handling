
# import

import keyword # 모듈 임포트
py_keyword = keyword.kwlist # 키워드 반환
print('파이썬 키워드:', py_keyword)
print('len=', len(py_keyword)) #len= 35
import datetime # module 임포트
today = datetime.datetime.now() # module.class.method()
print(today) # 2020-04-07 11:10:23.061312




'''
비가 올 때 어떻게 대처할 것인지를 순서도로 그려보라. 
비가 오지 않으면 외출 한 다. 
비가 오면 우산을 가지고 있는지 검사한다. 
우산을 가지고 있다면 외출한 다. 
우산 을 가지고 있지 않다면 무한정 비가 그칠 때까지 기다린다. 
'''

rain = input('비가오는가? :')
if rain == '예' :
    check = input('우산이 있는가? :')
    if check == '예' :
        print('외출한다')
    else :
        print('기다린다')
else :
    print('외출한다')


while True :
    rain = input('비가오는가? :')
    if rain == '예':
        check = input('우산이 있는가? :')
        if check == '예':
            print('외출한다')
        else:
            print('기다린다')
            break
    else:
        print('외출한다')


'''
사용자로부터 
임의의 개수의 성적을 받아서 평균을 계산한 후에 
출력하는 프로 그램 을 작성하여 보자. 
센티널로는 음수의 값을 사용하자. 
'''
tot = 0
cnt = 0
while True :
    score = int(input('성적을 입력하세요 :'))
    if score < 0 :
        break
    else :
        cnt += 1
        tot += score
print('평균 성적 =', tot/cnt)


l = []
for i in range(1,101) :
    l.append(i)
print(l)


'''
random과 range를 사용하여 특정범위에서 랜덤으로 숫자 뽑아내기
뽑아낸 숫자들로 분류정확도 만들기
'''




