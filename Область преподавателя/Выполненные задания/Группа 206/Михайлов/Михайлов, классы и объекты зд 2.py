class BankAccount:
    def __init__(self, number, sum):
        self.account_number = number 
        self.balance = sum 
        print(f"Создан счет. Начальный баланс: {sum} монет")

    def add(self, sum):
        self.balance = self.balance + sum
        print(f"На счет зачислено: {sum} монет")

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance = self.balance - sum
            print(f"Со счета снято {sum} монет")
        else:
            print(f"Недостаточно монет на счете")


acc1 = BankAccount("1234577", 1000)
acc1.add(200)
acc1.withdraw(500)
acc1.withdraw(300)
acc1.withdraw(900)


input()