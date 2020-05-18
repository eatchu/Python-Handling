'''
 <급여 계산 문제>
문) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 구현하시오.
    <조건> pay_pro 함수 재정의     
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
    
    # 원형 함수 : 급여 계산 함수     
    def pay_pro(self):
        pass

# 자식클래스 - 정규직 
class Permanent(Employee):

    def __init__(self,name):
        self.name = name

    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self, ppay, bonus):
        self.pay = ppay + bonus
        print('정규직 {} 사원 급여 : {}'.format(self.name, self.pay))


# 자식클래스 - 임시직 
class Temporary(Employee):

    def __init__(self,name):
        self.name = name
    
    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self, time, tpay):
        self.pay = time * tpay
        print('임시직 {} 사원 급여 : {}'.format(self.name, self.pay))
    
    
worker1 = Permanent('홍길동')
worker1.pay_pro(1000, 2000) # 정규직 홍길동 사원 급여 : 3000
    
worker2 = Temporary('이순신')
worker2.pay_pro(10, 2000) # 임시직 이순신 사원 급여 : 20000
