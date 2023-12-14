class BankAccount:
    def __init__(self, account_number, _balance):
        self.account_number = account_number
        self._balance = _balance  # _balance is a protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def __deduct_fee(self, fee):
        if fee > 0 and fee <= self._balance:
            self._balance -= fee
            print(f"Fee deducted. New balance: {self._balance}")
        else:
            print("Invalid fee or insufficient balance.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def process_monthly_fee(self):
        # This method is using a protected method _deduct_fee
        self.__deduct_fee(10)  # Example: Deducting a monthly fee


account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
account.process_monthly_fee()
