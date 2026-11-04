class BankAcct:
    # Initialize the bank account.
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Adjust the interest rate.
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Withdraw money from the account.
    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            return True
        return False

    # Deposit money into the account.
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            return True
        return False

    # Return the current balance.
    def get_balance(self):
        return self.amount

    # Calculate interest based on the number of days.
    def calculate_interest(self, days):
        return self.amount * (self.interest_rate / 100) * (days / 365)

    # Display account information.
    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate:.2f}%"
        )


# Test the BankAcct class.
def test_bank_account():
    # Create an account.
    account = BankAcct("John Smith", "123456789", 1000.00, 5.0)

    print("----- Bank Account Test -----")
    print(account)

    # Test deposit.
    print("\nDepositing $250.00...")
    account.deposit(250.00)
    print(f"New Balance: ${account.get_balance():.2f}")

    # Test withdrawal.
    print("\nWithdrawing $100.00...")
    account.withdraw(100.00)
    print(f"New Balance: ${account.get_balance():.2f}")

    # Test interest calculation.
    print("\nCalculating interest for 30 days...")
    interest = account.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    # Test changing the interest rate.
    print("\nAdjusting interest rate to 6.0%...")
    account.adjust_interest_rate(6.0)
    print(f"New Interest Rate: {account.interest_rate:.2f}%")

    # Calculate interest with the new rate.
    interest = account.calculate_interest(30)
    print(f"Interest for 30 days at new rate: ${interest:.2f}")

    # Display final account information.
    print("\n----- Final Account Information -----")
    print(account)


# Run the test function.
if __name__ == "__main__":
    test_bank_account()
