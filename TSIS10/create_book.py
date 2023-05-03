import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="12345")

command = """CREATE TABLE phonebook (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone_number VARCHAR(20)
);"""
conn.autocommit = True

cursor = conn.cursor()

cursor.execute(command)

cursor.close()
conn.close()
