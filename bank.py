#Name: Jason Palomo
#Date: 07/14/2020
#Program Description: Bank account transactions for checking and savings

class BankAccount:
    #Parent class for Bank Transactions
    
    def __init__(self,accountNumber, balance):
        #Initialize BankAccount attributes.
        self.accountNumber = accountNumber
        self.balance = balance

    def withdrawl_funds(self, withdrawlAmount):
        self.balance = int(self.balance) - int(withdrawlAmount) 

    def deposit_funds(self, depositAmount):
        self.balance = int(self.balance) + int(depositAmount)

    def get_balance(self):
        #Print a statement showing the balance of the account
        print(f"${self.balance}")

class CheckingAccount(BankAccount):
    #Child class of BankAccount Class 

    def __init__(self, accountNumber, balance, fees, min_balance):
        #Initialize attributs of the parent class
        super().__init__(accountNumber, balance)
        self.min_balance = min_balance
        self.fees = fees
        self.check_min_balance()

    def check_min_balance(self):    
        if self.balance < self.min_balance:
            print(f"You account balance of ${self.balance} is below the minumum balace requirement.")
        else:
            print(f"Your balance of ${self.balance} is fine. ")
    
    def deduct_fees(self):
        self.balance = int(self.balance) - int(self.fees)

class SavingAccount(BankAccount):
    #Child class of BankAccount Class

    def __init__(self, accountNumber, balance):
        #Initialize attributes of parent class
        super().__init__(accountNumber, balance)
        self.interest = float(0.02)

    def add_interest(self):
        self.balance = self.balance + (self.balance * (self.interest / 12))
        self.balance = round(self.balance, 2)



my_checking1 = CheckingAccount(1234,49)
my_checking2 = CheckingAccount(12345, 100)
