# Raise an exception
# to throw (or raise) an exception, use the raise keyword.

x = -1


# if x < 0:
#     raise Exception("Sorry, no numbers below zero")
# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

# Custom Exception
class WithdrawalError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient balance ({balance}) for withdrawal of {amount}.")


def perform_withdrawal(balance, amount):
    if amount > balance:
        raise WithdrawalError(balance, amount)
    # Process the withdrawal logic here
    return f"Withdrawal of {amount} successful. New balance: {balance - amount}"


# Example usage:
try:
    account_balance = 500
    withdrawal_amount = 700
    result = perform_withdrawal(account_balance, withdrawal_amount)
    print(result)
except WithdrawalError as e:
    print(f"Error: {e}")
finally:
    print("program completed")
