class BankAccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self._balance += amount

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        """check the balance"""
        return self._balance

    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.balance})'.format(self)

    def __str__(self):
        return 'Bank account of {}, current balance: {}'.format(self.name, self.balance)