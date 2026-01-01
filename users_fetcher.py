import requests

get = requests.get("https://jsonplaceholder.typicode.com/users")
users = get.json()

for user in users:
    name = user["name"]
    email = user["email"]
    print(f"Имя: {name} | Почта: {email}")
name = user["name"]
email = user["email"]
with open("users.txt", "w") as f:
    for user in users:
        name = user["name"]
        email = user["email"]
        f.write(f"Имя: {name} | Email: {email}\n")