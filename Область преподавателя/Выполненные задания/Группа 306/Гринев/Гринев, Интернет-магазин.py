class User:
    def __init__(self, firstname, lastname, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address

    def change_firstname(self, new_firstname):
        if isinstance(new_firstname, str) and new_firstname.strip():
            self.firstname = new_firstname
            return True
        return False

    def change_lastname(self, new_lastname):
        if isinstance(new_lastname, str) and new_lastname.strip():
            self.lastname = new_lastname
            return True
        return False

    def change_email(self, new_email):
        if "@" in new_email and len(new_email.split("@")) == 2:
            self.email = new_email
            return True
        return False

    def change_address(self, new_address):
        if isinstance(new_address, str) and new_address.strip():
            self.address = new_address
            return True
        return False

    def __str__(self):
        return (f"User(Firstname: {self.firstname}, Lastname: {self.lastname}, "
                f"Email: {self.email}, Address: {self.address})")

# Создание экземпляра пользователя
user = User("John", "Doe", "john.doe@example.com", "123 Main St")

# Проверка начального состояния
print(user)

# Изменяем переменные экземпляра
print("Changing firstname:", user.change_firstname("Jane"))  # Успешно
print("Changing lastname:", user.change_lastname("Smith"))  # Успешно
print("Changing email:", user.change_email("jane.smith@example.com"))  # Успешно
print("Changing address:", user.change_address("456 Elm St"))  # Успешно

# Проверка состояния после изменений
print(user)

# Пытаемся установить некорректные значения
print("Trying to change email to invalid:", user.change_email("invalidemail"))  # Неуспешно
print("Trying to change address to empty string:", user.change_address(""))  # Неуспешно

# Проверка финального состояния
print(user)

input()