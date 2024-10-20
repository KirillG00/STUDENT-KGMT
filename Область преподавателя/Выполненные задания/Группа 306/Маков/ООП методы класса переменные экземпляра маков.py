class User:
    def __init__(self, firstname, lastname, email, address):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address

    def change_firstname(self, new_firstname):
        if isinstance(new_firstname, str) and new_firstname:
            self.firstname = new_firstname
            return True
        return False

    def change_lastname(self, new_lastname):
        if isinstance(new_lastname, str) and new_lastname:
            self.lastname = new_lastname
            return True
        return False

    def change_email(self, new_email):
        if "@" in new_email and "." in new_email.split("@")[-1]:
            self.email = new_email
            return True
        return False

    def change_address(self, new_address):
        if isinstance(new_address, str) and new_address:
            self.address = new_address
            return True
        return False


user = User("John", "Doe", "john.doe@example.com", "123 Elm St")
print(user.change_email("new.email@example.com"))  # True
print(user.change_firstname("Jane"))                # True
print(user.change_address(""))                        # False
print(user.change_lastname("Smith"))                # True

input()