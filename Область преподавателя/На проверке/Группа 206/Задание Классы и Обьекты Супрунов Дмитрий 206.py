class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def add(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На счет добавлено {amount}. Текущий баланс: {self.balance}.")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете.")
        elif amount <= 0:
            print("Сумма должна быть положительной.")
        else:
            self.balance -= amount
            print(f"С счета снято {amount}. Текущий баланс: {self.balance}.")

# Пример использования
account1 = BankAccount("123456789", 1000)

account1.add(500)
account1.withdraw(200)
account1.withdraw(1500)  # Попытка снять больше, чем есть на счете