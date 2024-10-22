class BankAccount:
    def __init__(self, account_number,
initial_balance=0):
     def add(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На счет
{self.account_number} добавлено {amount}. 
Новый баланс: {self.balance}.")
        else:
            print("Сумма для добовления должна быть положительной.")
    def withdraw(self, amount):
       if amount > self.balance:
          print("Недостаточно средств на счете.")

       elif amount > 0:
           self.balance -= amount
           print(f"C Cчета{self.account_number} снято {amount}.
                Остаток на счете: {self.balance}.")
       else:
          print("Cумма для снятия должна быть положительной")
        

account = BankAccount("123456789", 1000)

account.add(400)
account.withdraw(200)
account.withdraw(1500)