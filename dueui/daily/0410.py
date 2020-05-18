# 사용자 정의 함수의 디폴트 인수
def call(name,msg='수고했어') :
    print(msg)
    print('%s야'%(name))
    print(f'정말 {msg}')
call('두의')
'''
수고했어
두의야
정말 수고했어
'''

# 사용자 정의 함수 값에 의한 호출
def call2(name) :
    name += '바보'
    return name


def sub():
    global s
    print(s)
    s = " 바나나가좋음 !"
    print(s)

s = " 사과가좋음 !"
sub()
print(s)


from scatter.scatter_module import Avg, var_std
def statis(func,*data) :
    if func == 'sum' :
        return sum(data) # 함수 실행 종료(exit)
    elif func == 'avg' :
        return Avg(data)
    elif func == 'var' :
        var, std = var_std(data)
        return var
    elif func == 'std' :
        var, std = var_std(data)
        return std
    else :
        return '해당 함수 없음'
print(statis('std',1,2,3,4,5))

'''
식별자 
캐멀케이스 : 대문자로 시작 -> 클래스
스네이크케이스 : 소문자로 시작 -> 함수 or 변수
'''

print('{:g}'.format(52.0000))
