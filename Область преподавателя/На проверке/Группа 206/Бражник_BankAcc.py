class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def add(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Добавлено {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете.")
        elif amount <= 0:
            print("Сумма должна быть положительной.")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Новый баланс: {self.balance}")

if __name__ == "__main__":
    account = BankAccount("123456789", 1000)
    account.add(550)
    account.withdraw(200)
    account.withdraw(1300)