import sqlite3
import requests
try:
    pinus = requests.get("https://jsonplaceholder.typicode.com/albums", timeout=5)
    pinus.raise_for_status()
    albums = pinus.json()
except requests.exceptions.RequestException as e:
    print(f"Ошибка при загрузке данных: {e}")
    albums=[]

conn = sqlite3.connect("album.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS albums(
        id INTEGER PRIMARY KEY,
        title TEXT)
    """)
try:
    for album in albums:
        cursor.execute(
        "INSERT INTO albums (id, title) VALUES (?, ?)",
        (album["id"], album["title"])
        )
except sqlite3.IntegrityError:
    print("Ошибка в записывании файла! У вас уже есть файл! Ниже существующие записи в файле:")
cursor.execute("SELECT title FROM albums WHERE id LIMIT 5")
results = cursor.fetchall()
for row in results:
    print(row[0])

conn.commit()
conn.close()