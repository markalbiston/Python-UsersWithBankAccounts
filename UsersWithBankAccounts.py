#--------unable to get multiple accounts to work yet....

class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        # self.account_balance = 0
        self.account = BankAccount(account_name='', int_rate=0.004, balance=0)
    
    def make_deposit(self, amount, account_name):
        # self.account_balance += amount
        self.account.deposit(amount, account_name)
        return self

    def make_withdrawal(self, amount, account_name):
        self.account.withdraw(amount, account_name)
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     other_user.account_balance += amount
    #     return self

    def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.account.account_balance}")
        # print(f"User: {self.name}, {self.account.display_account_info()}")
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, account_name, int_rate=0.004, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance
        
    def deposit(self, amount, account_name):
        self.account_balance += amount
        return self

    def withdraw(self, amount, account_name):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Current {self.account_name} Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        # self.account_balance = self.account_balance * (1+self.int_rate)
        self.account_balance *= (1+self.int_rate)
        return self

#create instances of class User
luke = User("Luke", "luke@me.com")
gus = User("Gus", "gus@me.com")

#create instances of class BankAccount
checking = BankAccount('Checking',0.001)
savings = BankAccount('Savings',0.004)

luke.make_deposit(500,checking).make_deposit(500,'Checking').make_deposit(200,'Savings').make_withdrawal(250,'Checking').account.yield_interest()
luke.display_user_balance()
gus.make_deposit(300,checking).make_deposit(150,savings).make_deposit(200,savings).make_withdrawal(50,checking).account.yield_interest()
gus.display_user_balance()


