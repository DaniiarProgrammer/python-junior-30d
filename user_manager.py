import json
import sqlite3
import requests

get = requests.get("https://jsonplaceholder.typicode.com/users")
users = get.json()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        email TEXT,
        password TEXT)
    """)


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

    def save_to_db(self):
        for user in self.users:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES(?, ?, ?)",
                (user.name, user.email, user.password)
            )
        conn.commit()
    
    def load_from_db(self):
        cursor.execute("SELECT name, email, password FROM users")
        rows = cursor.fetchall()
        self.users = []
        for row in rows:
            user = User(row[0], row[1], row[2])
            self.users.append(user)

if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Пинус", "Pinus@gmail.com", "!@21449#%^&*&$!151")
    manager.print_all_users()
    manager.save_to_json("users.json")

    new_manager = UserManager()
    new_manager.load_from_json("users.json")
    new_manager.print_all_users()

    manager.save_to_db()

    db_manager = UserManager()
    db_manager.load_from_db()
    print("\nЗагружено из БД: ")
    db_manager.print_all_users()

conn.close()