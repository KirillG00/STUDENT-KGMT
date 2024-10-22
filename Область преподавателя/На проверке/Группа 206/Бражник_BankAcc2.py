class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self._owner = owner
        self.balance = balance

    def get_owner(self):
        return self._owner

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

# Пример использования класса
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 1000)
    print(f"Владелец счета: {account.get_owner()}")
    try:
        account._owner = "Jane Smith"
    except AttributeError as e:
        print(f"Ошибка: {e}")

    account.add(1000)
    account.withdraw(500)
    account.withdraw(1000)