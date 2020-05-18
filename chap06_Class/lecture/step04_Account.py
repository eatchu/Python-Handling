'''
중첩함수 -> 클래스
'''

class Account :
    # outer -> 멤버변소
    # balance = 0

    def __init__(self,bal):
        self.balance = bal

    # inner -> 멤버메소드
    def getBalance(self):
        return self.balance

    def deposit(self, money):  # 입금하기(setter)
        if money < 0 :
            print('금액을 확인하세요.')
        else :
            self.balance += money

    def withdraw(self, money):  # 출금하기(setter)
        if self.balance >= money:
            self.balance -= money
        else:
            print('잔액이 부족합니다')

acc = Account(1000)
acc.getBalance() # 1000
acc.deposit(20000)
acc.getBalance() # 21000
acc.withdraw(5000)
acc.getBalance() # 16000





class bank_account:
    balance = 0  # 잔액(balance)

    def data(self, balance):
        self.balance = balance

    def getBalance(self):  # 잔액확인(getter)
        print('현재 계좌 잔액은 {}원 입니다.'.format(self.balance))

    def deposit(self):  # 입금하기(setter)
        money = int(input('입금액을 입력하세요 : '))
        self.balance += money
        print('{}원 입금후 잔액은 {}원 입니다.'.format(money, self.balance))

    def withdraw(self):  # 출금하기(setter)
        money = int(input('출금액을 입력하세요 : '))
        if self.balance >= money:
            self.balance -= money
            print('{}원 출금후 잔액은 {}원 입니다.'.format(money, self.balance))
        else:
            print('잔액이 부족합니다')


count = bank_account()
count.data(30000)
count.getBalance()
count.deposit()
count.withdraw()


count2 = bank_account(1000) # error

'''
1. 예금자(accName), 계좌번호(accNo) 동적 멤버변수 추가하기
   -> 예금자 : 홍길동, 계좌변호 : 012-125-41520
2. getBalance() 메소드를 이용하여 계좌, 예금주 계좌번호 출력하기
'''

