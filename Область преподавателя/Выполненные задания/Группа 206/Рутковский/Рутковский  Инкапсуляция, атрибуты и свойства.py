class BankAccount:
    def __init__(self):
        self.__balance = 0  # Закрытый атрибут для хранения баланса

    def deposit(self, amount):
        """Метод для внесения суммы на счет."""
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount}. Новый баланс: {self.__balance}.")
        else:
            print("Ошибка: Сумма должна быть положительной.")

    def withdraw(self, amount):
        """Метод для снятия суммы со счета."""
        if amount > self.__balance:
            print("Ошибка: Недостаточно средств на счете.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Снято {amount}. Остаток на счете: {self.__balance}.")
        else:
            print("Ошибка: Сумма должна быть положительной.")

    @property
    def balance(self):
        """Свойство для получения текущего баланса."""
        return self.__balance

# Пример использования класса BankAccount
account = BankAccount()

account.deposit(500)   # Внесение 500
account.withdraw(200)   # Снятие 200
print(f"Текущий баланс: {account.balance}")  # Получение текущего баланса
account.withdraw(400)   # Попытка снять больше, чем на счете
account.deposit(-100)   # Попытка внести отрицательную сумму

input()
