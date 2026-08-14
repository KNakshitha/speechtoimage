import sqlite3

conn = sqlite3.connect("images.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS images(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
image_file TEXT
)
""")

data = [
("cat","cat.jpg"),
("car","car.jpg"),
("tree","tree.jpg"),
("monkey","monkey.jpg"),
("lion","lion.jpg"),
("tiger","tiger.jpg"),
("mouse","mouse.jpg"),
("computer","computer.jpg"),
("elephant","elephant.jpg"),
("earphone","earphone.jpg"),
("python","python.jpg")
]

cursor.executemany("INSERT INTO images(name,image_file) VALUES(?,?)",data)

conn.commit()
conn.close()

print("Database created")