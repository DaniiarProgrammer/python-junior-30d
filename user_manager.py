import json

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
        return{"Имя": self.name, "email": self.email, "Пароль": self.password}


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email, password):
        user = User(name,email,password)
        self.users.append(user)

    def save_to_json(self, filename):
        data = [user.to_dict() for user in self.users]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.users = []
        for item in data:
            user = User(item["Имя"], item["email"], item["Пароль"])
            self.users.append(user)

    def print_all_users(self):
        for user in self.users:
            print(f"Имя: {user.name}, Email: {user.email}")

if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Данияр", "daniiar@gmail.com", "!@21449#%^&*&$!151")
    manager.print_all_users()
    manager.save_to_json("users.json")

    new_manager = UserManager()
    new_manager.load_from_json("users.json")
    new_manager.print_all_users()