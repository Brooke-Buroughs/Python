class BankAccount:
    bank_name="Bank of Dojo"
    def __init__(self,int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"Account total:{self.balance}")
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a fee of $5")
            self.balance-=5
        return self
    @staticmethod
    def can_withdraw(balance,amount):
        if(balance-amount)<0:
            return False
        else:
            return True
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        return self

Brooke=BankAccount(.01,100)
Brooke.deposit(20).deposit(40).deposit(50).withdraw(100).display_account_info().yield_interest().display_account_info()
Bradley=BankAccount(.05,300)
Bradley.deposit(176.25).deposit(319.01).withdraw(48.97).withdraw(10.12).withdraw(195).withdraw(50).yield_interest().display_account_info()



