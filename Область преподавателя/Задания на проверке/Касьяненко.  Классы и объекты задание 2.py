#Классы и объекты задание 1
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # Номер счета
        self.balance = initial_balance  # Баланс счета

    def add(self, amount):
        """Метод для добавления суммы на баланс."""
        if amount > 0:
            self.balance += amount
            print(f"На счет {self.account_number} добавлено {amount}. Новый баланс: {self.balance}.")
        else:
            print("Сумма для добавления должна быть положительной.")

    def withdraw(self, amount):
        """Метод для снятия суммы с баланса."""
        if amount > self.balance:
            print("Недостаточно средств на счете.")
        elif amount > 0:
            self.balance -= amount
            print(f"С счета {self.account_number} снято {amount}. Остаток на счете: {self.balance}.")
        else:
            print("Сумма для снятия должна быть положительной.")

# Пример использования класса BankAccount
account = BankAccount("342112", 1000)

account.add(600)      # Добавление 600
account.withdraw(400)  # Снятие 400
account.withdraw(1500) # Попытка снять больше, чем на балансе
