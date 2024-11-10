class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    def add(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На счет"
                  f" {self.account_number} добавлено {amount}."
                  f" Новый баланс {self.balance}")
            if amount > self.balance:
                print("Недостаточно средств на счете")
            elif amount > 0:
                self.balance -= amount
                print(f"С счета"
                      f" {self.account_number} снято {amount}."
                      f" Остаток на счете: {self.balance}.")
            else:
                print("Сумма для снятия должна быть положительной.")
account = BankAccount("123456789", 100)
account.add(100)

#Условие выполненно не до конца. По условию нужно добавить метод, который 
# добавляет средства на счет и метод, который снимает.
