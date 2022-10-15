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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # other methods
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.display_account_info)
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        print(self.account.display_account_info)

Brooke=BankAccount(.01,100)
Brooke.deposit(20).deposit(40).deposit(50).withdraw(100).display_account_info().yield_interest().display_account_info()
Bradley=BankAccount(.05,300)
Bradley.deposit(176.25).deposit(319.01).withdraw(48.97).withdraw(10.12).withdraw(195).withdraw(50).yield_interest().display_account_info()

#Sensei Bonus: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
#Senpai Bonus: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.