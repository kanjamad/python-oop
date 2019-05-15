# bank account class
class BankAccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self.balance += amount

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self): #are accessor methods needed in Python?
        """check the balance"""
        return self.balance


def main():
    customer1 = BankAccount('Alex')
    print(customer1.get_balance())
    customer1.deposit(100)
    customer1.withdraw(30)
    print(customer1.get_balance())

    customer2 = BankAccount('Sam', 200)
    print(customer2.get_balance())

if __name__ == "__main__":
    main()