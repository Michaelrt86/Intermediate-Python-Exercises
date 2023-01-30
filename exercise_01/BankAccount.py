class BankAccount(object): 
    def __init__(self, name, balance):
            self.name = name
            self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print('You have successfully deposited: ' + self)
        print('Account balance: ',self.balance)

    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        print('You have successfully deposited: ' + self)
        print('Account balance: ',self.balance)

    def get_balance(self):
        print(self.name,' has a balance of ',self.balance) 