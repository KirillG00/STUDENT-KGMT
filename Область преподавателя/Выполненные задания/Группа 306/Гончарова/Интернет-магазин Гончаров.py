#Создайте класс, который описывает пользователя в интернет-магазине. Создайте переменные экземпляра: firstname, lastname, email, address.
#Создайте методы, которые будут изменять отдельные переменные экземпляра. В этих методах проверьте правильность вводимых данных.
#Создайте пользователя и проверьте работу методов.


class User:
    def __init__(self, firstname, lastname, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address

    def set_firstname(self, firstname):
        if len(firstname) > 0:
            self.firstname = firstname
        else:
            print("Ошибка")

    def set_lastname(self, lastname):
        if len(lastname) > 0:
            self.lastname = lastname
        else:
            print("Ошибка")

    def set_email(self, email):
        if "@" in email and "." in email:
            self.email = email
        else:
            print("Ошибка")

    def set_address(self, address):
        if len(address) > 0:
            self.address = address
        else:
            print("Ошибка")

user1 = User("Дандуров", "Максим", "hgtftfrtrgrgsr@example.com", "улица Пушкина, -00000")

user1.set_firstname("Добротин")
user1.set_lastname("Карен")
user1.set_email("neeeeeeet@example.com")
user1.set_address("Улица Никитушки, 528")

print("First Name:", user1.firstname)
print("Last Name:", user1.lastname)
print("Email:", user1.email)
print("Address:", user1.address)

input()