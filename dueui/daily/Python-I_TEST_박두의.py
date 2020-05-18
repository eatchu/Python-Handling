'''
Python-I TEST
 파일명 : Python-I_TEST_홍길동.py
 메일 전송 : kpjiju@naver.com
'''

'''
chap02_Control ~ chap03_DataSet 관련문제

[문1] 교차검정 dataset 생성하기
  - 교차검정 : train과 test 셋을 cross check 하여 모델을 검정하는 방법

<< 출력 화면 예시>>
검정 데이터 : 1
훈련 데이터 : [2, 3, 4, 5]
검정 데이터 : 2
훈련 데이터 : [1, 3, 4, 5]
검정 데이터 : 3
훈련 데이터 : [1, 2, 4, 5]
검정 데이터 : 4
훈련 데이터 : [1, 2, 3, 5]
검정 데이터 : 5
훈련 데이터 : [1, 2, 3, 4]
'''

# 방법 1
dataset = [1,2,3,4,5] # 교차검정 dataset

test = 0 # 검정 데이터

for i in dataset :
    dataset = [1, 2, 3, 4, 5]
    test = i
    dataset.remove(i)
    print('검정데이터 : %d'%(test))
    print('훈련데이터 :', dataset)


# 방법 2
dataset = [1,2,3,4,5] # 교차검정 dataset

test = 0 # 검정 데이터
train = [] # 훈련 데이터

for i in range(5) :
    test = dataset[i]
    train = dataset[:i] + dataset[i+1:]
    print('검정 데이터 :',test)
    print('훈련 데이터 :',train)


# 방법 3
dataset = [1,2,3,4,5] # 교차검정 dataset
for i in dataset :
    train = []
    print('검정 데이터: {}'.format(i))
    for j in dataset:
        if i != j:
            train.append(j)
    print('훈련 데이터: {}'.format(train))



'''
- chap04_regExText ~ chap05_Function 관련 문제
[2문] 다음 벡터(pay)는 '입사년도사원명급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 아래와 같은 출력결과가 나타나도록 함수를 정의하시오. 

   <출력 결과>
 전체 급여 평균 : 260
 평균 이상 급여 수령자
 이순신 => 300 
 유관순 => 260 
'''

# 방법 1
pay = ["2014홍길동220", "2002이순신300", "2010유관순260"]
pay1 = []

# 함수 정의
def pay_pro(pay):
    from statistics import mean # 평균
    from re import findall
    
    ### 평균급여 ###
    pay1 = [int(findall('[0-9]{3}$',i)[0]) for i in pay]
    avg = mean(pay1)
    print('전체급여평균 : %d' % (avg))

    # 평균 급여 이상 수령자
    print('평균 이상 급여 수령자')
    for j in pay :
        if int(findall('[0-9]{3}$',j)[0]) >= avg :
            print(findall('\D{3}',j)[0],'->',int(findall('[0-9]{3}$',j)[0]))

# 함수 호출
pay_pro(pay)
'''
전체급여평균 : 260
평균 이상 급여 수령자
이순신 -> 260
유관순 -> 260

'''

# 방법 2
pay = ["2014홍길동220", "2002이순신300", "2010유관순260"]

from statistics import mean # 평균
from re import findall  # 정규표현식
# 함수 정의
def pay_pro(x):
    data = dict()
    salary = []
    for word in x:
        data[findall('[가-힣]{3,}', word)[0]] = findall('\d{3}', word)[1]
        salary.append(int(findall('\d{3}', word)[1]))

    mu = mean(salary)
    print("전체 급여 평균 : {}".format(mu))
    print("평균 이상 급여 수령자")
    for k,v in data.items():
        if int(v) >= mu:
            print("{} => {}".format(k,v))

# 함수 호출
pay_pro(pay)

# 방법 3
pay = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def pay_pro(x):
    from statistics import mean # 평균
    import re # 정규표현식

    name = list()
    sal = list()
    for i in x:
        name.append(re.findall('[가-힣]+', i)[0])
        sal.append(int(re.findall(r'\d+$', i)[0]))

    print(f'전체 급여 평균 : {mean(sal)}\n평균 이상 급여 수령자')

    for idx, val in enumerate(sal):
        if val >= mean(sal):
            print(f'{name[idx]} => {sal[idx]}')

# 함수 호출
pay_pro(pay)





'''
 chap05_Function 관련 문제 
 [문3] student(3명의 학생 점수)를 이용하여 다음 조건에 맞게 학생관리 프로로그램의
       함수로 완성하시오.
  <조건1> outer : students() -> 제목(title) 출력 , inner 함수 포함  
  <조건2> inner : tot_age_calc()  -> 총점과 평균 계산 반환
          inner : score_display() -> 학생 이름과 과목점수, 총점, 평균 출력 
  <조건3> 기타 나머지는 출력 예시 참조           

            <<출력 예시>>
    *** 2018년도 2학기 성적처리 결과 ***
-----------------------------------------    
 번호  국어   영어  수학   총점    평균
-----------------------------------------
  1.   90    85    70    245    81.67
  2.   99    90    95    284    94.67
  3.   70    80    100   250    83.33
------------------------------------------
'''
#  [국어,영어,수학]
hong = [90, 85, 70]
lee = [99, 90, 95]
yoo = [70, 80, 100]
student = [hong, lee, yoo]
# [[90, 85, 70], [99, 90, 95], [70, 80, 100]]


def Students(student):
    score = student

    # 평균, 총점 계산
    def tot_age_calc():
        from statistics import mean
        for j in score:
            a = sum(j)
            b = round(mean(j), 2)
            j.append(a)
            j.append(b)
        score_tot = score
        return score_tot

    # 점수 출력
    def score_display(score_tot):
        print('\n\t*** 2018년도 2학기 성적처리 결과 ***')
        print('-' * 50)
        print("번호 국어 영어 수학  총점  평균")
        print('-' * 50)
        for i in range(3) :
            print(' %d.  %d  %d   %d   %d   %.2f'
                  %(i+1,score_tot[i][0],score_tot[i][1],score_tot[i][2],score_tot[i][3],score_tot[i][4]))
        print('-' * 50)

    return tot_age_calc, score_display



# outer 함수 호출
final, show = Students(student)
# 평균 총합 만들기
score=final()
# 점수 출력
show(score)




'''
	*** 2018년도 2학기 성적처리 결과 ***
--------------------------------------------------
번호 국어 영어 수학  총점  평균
--------------------------------------------------
1 [90, 85, 70, 245, 81.67]
2 [99, 90, 95, 284, 94.67]
3 [70, 80, 100, 250, 83.33]
--------------------------------------------------

'''




'''
 chap06_Class 관련 문제 
 [문4] 문3의 내용을 클래스로 구현하시오.
'''

class Student :
    def __init__(self, student):
        self.score = student
    def tot_age_calc(self):
        from statistics import mean
        for j in self.score:
            a = sum(j)
            b = round(mean(j), 2)
            j.append(a)
            j.append(b)

    def score_display(self):
        print('\n\t*** 2018년도 2학기 성적처리 결과 ***')
        print('-' * 50)
        print("번호 국어 영어 수학  총점  평균")
        print('-' * 50)
        for i in range(3) :
            print(i+1 ,   self.score[i])
        print('-' * 50)
# 객체 생성
final2 = Student(student)
# 평균 총합 계산
final2.tot_age_calc()
# 점수 출력
final2.score_display()





