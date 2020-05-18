'''
함수의 가변인수
 - 한 개의 가인수로 여러 개의 실인수를 받는 인수
 형식) def 함수명(*인수)
'''

# 1. tuple형으로 받는 가변인수
def Func1(name,*names) :
    print(name)
    print(names)
Func1('홍길동','이순신','유관순')


# 패키지.모듈
'''
외부에서 작업한 사용자 정의함수를 가져와서 사용할 수 있다
'''
import scatter.scatter_module
from scatter.scatter_module import Avg, var_std

datas = [2,3,5,6,7,8.5]
Avg(datas) # 5.25

var,std = var_std(datas)
print(var,std) # 5.975 2.444381312316063


def statis(func,*data) :
    if func == 'sum' :
        return sum(data) # 함수 실행 종료(exit)
    elif func == 'avg' :
        return Avg(data)
    elif func == 'var' :
        return var_std(data)
    elif func == 'std' :
        return var_std(data)
    else :
        return '해당 함수 없음'

var, _ = statis('var',1,2,3,4,5)
print(var)
_ , std = statis('var', 1, 2, 3, 4, 5)
print(std)

'''
정의된 함수에 값이 두개이상 return이 되는데 값을 한개만 보고 싶을때는
사용하지 않을 변수명을 _ 로 지정하면 값을 받긴받되 출력되지 않는다
'''


def statis(func,*data) :
    if func == 'sum' :
        return sum(data) # 함수 실행 종료(exit)
    elif func == 'avg' :
        return Avg(data)
    elif func == 'var' :
        var,std = var_std(data)
        return var
    elif func == 'std' :
        var,std = var_std(data)
        return std
    else :
        return '해당 함수 없음'

print(statis('std',1,2,3,4,5))





# 2. dict형 가변인수
def person(w,h,**other) :
    print(w)
    print(h)
    print(other) # 'name':'홍길동', 'age':35
person(65, 175, name='홍길동', age=35)
person(65, 175, '홍길동', 35) # error

'''
* : 나머지 원소를 tuple 형태로 받는다
** : 나머지 원소를 dict 형태로 받는다
'''



# 3. 함수를 인수로 받기
def square(x) :
    return x**2

def my_fnc(func, datas) :
    result = [func(d) for d in datas]
    return result

data = [1,2,3,4,5]
result = my_fnc(square, data)
print(result)


