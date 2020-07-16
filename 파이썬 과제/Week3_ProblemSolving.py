import random

class Account:
    num_account = 0
    account_list = []

# str(random.randint(1, 999)).zfill(3)
# str(random.randint(1,99)).zfill(2)
# str(random.randint(1,999999)).zfill(6)
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance  # 잔액
        self.account_number = str(random.randint(1, 999)).zfill(3) + "-" + str(random.randint(1, 99)).zfill(2) + "-" + str(random.randint(1, 999999)).zfill(6)  # 계좌 번호

        self.num_deposit = 0  # 입금 횟수
        self.bank = "SC은행"

        self.d_history = []
        self.w_history = []

        Account.num_account += 1  # 계좌(인스턴스) 생성시 1씩 증가
        Account.account_list.append(self)  # 계좌 생성시 리스트에 인스턴스 등록

# 생성된 계좌의 개수 출력
    @classmethod
    def get_account_num(cls):
        print(cls.num_account)
# 입금
    def deposit(self, money):
        self.num_deposit += 1
        self.d_history.append(money)
        if money >= 1:
            self.balance += money

        if self.num_deposit == 5:
            self.balance += (self.balance * 0.01)  # 입금 횟수 5회시 이자 지급

# 출금
    def withdraw(self, amount):
        self.w_history.append(amount)
        if amount <= self.balance:
            self.balance -= amount
# 정보 출력
    def display_info(self):
        print(f"""
은행이름: {self.bank}
예금주: {self.name}
계좌번호: {self.account_number}
잔고: {format(self.balance, ',')}원""")

    def deposit_history(self):
        print(f"{self.name}님의 예금 내역:")
        print(self.d_history)

    def withdraw_history(self):
        print(f"{self.name}님의 출금 내역:")
        print(self.w_history)

user_1 = Account("신짱구", 100000000)
user_2 = Account("신짱아", 200)
user_3 = Account("봉미선", 10000000)

user_1.deposit(300000)  # 과외비 입금
user_2.deposit(7777)    # 복권 7등 당첨
user_3.withdraw(33000)  # B마트 장보기
user_3.withdraw(230000)  # 짱아 피아노 레슨비
user_1.withdraw(423000)  # 액션가면 한정판 피규어 구입


user_1.deposit_history()
user_1.withdraw_history()
print()
user_2.deposit_history()
user_2.withdraw_history()
print()
user_3.deposit_history()
user_3.withdraw_history()


Account.get_account_num()

for i in range(len(Account.account_list)):
    if Account.account_list[i].balance >= 1000000:
        Account.account_list[i].display_info()

