'''
step2 관련 문제

문) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기 프로그램을 구현하시오. 
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''

print("==" * 15)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print("==" * 15)

coffee = 3
while True :
    money = int(input('지불할 금액 :'))
    left = money - 2500
    if money < 2500 :
        print('금액이 부족합니다.')
        continue
    elif money == 2500 :
        coffee = coffee - 1
        print('커피 맛있게 드세요')
        print('남은 커피는',coffee,'잔 입니다')
        if coffee == 0 :
            print('남은 커피 없어요 장사 끝!')
            break
    else :
        coffee = coffee - 1
        print('맛있게 드세요. 잔돈',left,'원 받으세요' )
        print('남은 커피는',coffee,'잔 입니다')

    if coffee == 0:
        print('남은 커피 없어요 장사 끝!')
        break

    
    
    
    
    