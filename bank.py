name = input('What is your name? ')
print('Hello *(' + name + ')* welcome to BankAccount')

class BankAccount():
    def __init__(self, account_type, name=''):
        self.name = name
        self.account_type = account_type
        self.balance = 0
        # print(name, "create =>", self)
    
    def __str__(self):
        return 'BankAccount -> type: {}, balance: {}'.format(self.account_type, self.balance)

    def bank_account(self):
        # print("Hello!!!! I have", self.savings,  "and In have" ,self.checking, )
        print('Hi! #(' + name +')# you have {} in savings {} in checking and balance is {}'.format(self.name, self.account_type, self.balance ))
        # print('There are {} in bank account total'.format(BankAccount.total_amount))

    # def deposit(self, amount):
    #     self.balance += amount
    #     print('New Balance = ', self.balance)
        
    # def withdraw(self, amount):
        
# kanjamad_account = BankAccount('Kanjamad', 'Savings')
# print(kanjamad_account.bank_account())

# kanjamad_account.deposit(50)

# print(kanjamad_account.bank_account())


kanjamad_savings = BankAccount('Savings', 'Kanjamad')
kanjamad_checking = BankAccount('Checking', 'Kanjamad')
print(kanjamad_savings)
print(kanjamad_checking)