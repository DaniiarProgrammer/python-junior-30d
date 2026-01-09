class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def is_password_strong(self):
        has_upper = any(char.isupper() for char in self.password)
        has_lower = any(char.islower() for char in self.password)
        has_special = any(char in "!@#$%^&*" for char in self.password)
        lenght = len(self.password)>12

        return all([has_lower, has_special, has_upper, lenght])
    
    def to_dict(self):
        return{"Имя": self.name, "email": self.email}

daniyar = User("Данияр", "daniiar@gmail.com", "!@21449#%^&*&$!151")
print(daniyar.to_dict())