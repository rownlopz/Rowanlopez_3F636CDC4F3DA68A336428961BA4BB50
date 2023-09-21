class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")

account1 = BankAccount(123456, "Rowan lopez", 1000)

account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()
