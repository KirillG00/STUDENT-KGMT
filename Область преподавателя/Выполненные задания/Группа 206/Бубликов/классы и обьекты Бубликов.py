class Rectangle:

    def __init__(self, width, length):
            self.width = width
            self.length = length

    def area(self):
        return (self.width * self.length)

    def perimeter (self):
       return 2 * (self.width + self.length)

rect = Rectangle(10,20)

print(f"Rectangle: width = {rect.width}, length = {rect.length}")
print(f"Rectangle area: Area = {rect.area()}")
print (f"Rectangle perimeter: Perimetr = {rect.perimeter()}")


class BankAccount:

    def __init__(self, number, sum):
        self.account_number = number
        self.balance = sum
        print(f"Создан счет. Начальный баланс: {sum} единиц")

    def add(self, sum):
        self.balance = self.balance + sum
        print(f"На счет зачислено: {sum} единиц")

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance = self.balance - sum
            print(f"Со счета снято: {sum} единиц")
        else:
            print("Недостаточно средств на счете")


acc1 = BankAccount("8888888", 1000)
acc1.add(200)
acc1.withdraw(500)
acc1.withdraw(300)
acc1.withdraw(900)

input()


