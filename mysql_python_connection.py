import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anju123@",
    database="training_db"
)

print("Connection status:", connection.is_connected())

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for record in records:
    print(record)

cursor.close()
connection.close()