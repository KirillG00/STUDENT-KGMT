class User:
    def __init__(self, firstname, lastname, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address

    def set_firstname(self, firstname):
        if isinstance(firstname, str) and firstname:
            self.firstname = firstname
        else:
            raise ValueError("Имя должно быть непустимой строкой.")

    def set_lastname(self, lastname):
        if isinstance(lastname, str) and lastname:
            self.lastname = lastname
        else:
            raise ValueError("Фамилия должна быть непустимой строкой.")

    def set_email(self, email):
        if isinstance(email, str) and "@" in email:
            self.email = email
        else:
            raise ValueError("Некорректный адрес электронной почты.")

    def set_address(self, address):
        if isinstance(address, str) and address:
            self.address = address
        else:
            raise ValueError("Адрес должен быть непустимой строкой.")


user = User("Иван", "Иванов", "ivan@example.com", "Москва, ул. Ленина, 1")

# Проверяем работу методов
user.set_firstname("Петр")
user.set_email("petr@example.com")

print(user.firstname, user.email)  # Вывод: Петр petr@example.com

input()