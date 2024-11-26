class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.__owner = owner
        self.__balance = balance
    @property
    def balance(self):
        return print("Ваш баланс:", self.__balance)
    def get_owner(self):
        return self.__owner

    def add(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Добавлено {amount}. Новый баланс: {self.__balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств на счете.")
        elif amount <= 0:
            print("Сумма должна быть положительной.")
        else:
            self.__balance -= amount
            print(f"Снято {amount}. Новый баланс: {self.__balance}")
        return self.__balance
# По условию необходимо добавить свойство balance (только для чтения),
# которое позволяет получить текущее значение баланса.

if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 0)
    print(f"Владелец счета: {account.get_owner()}")
    try:
        account.__owner = "Jane Smith"
    except AttributeError as e:
        print(f"Ошибка: {e}")
    account.add(1000)
    account.withdraw(500)
    account.withdraw(1000)
    account.balance
