class BankAccount:
    def __init__(self, owner):
        self.__balance = 0 
        self.__owner = owner  

    @property
    def balance(self):
        return self.__balance 

    @property
    def owner(self):
        return self.__owner  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
        else:
            print("Ошибка: сумма должна быть положительной!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Ошибка: недостаточно средств!")

    @owner.setter
    def owner(self, value):
        self._owner = value


account = BankAccount("John Doe")
print(account.balance)

account.deposit(1000)
print(account.balance) 

account.withdraw(500)  
print(account.balance) 

account.withdraw(1000)

print(account.owner)

try:
    account.owner = "Jane Smith" 
except AttributeError as e:
    print(e)
    
input()
