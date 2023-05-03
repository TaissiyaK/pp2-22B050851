import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="12345")

command = '''DELETE FROM phonebook 
            WHERE first_name = 'Jane' '''

conn.autocommit = True

cursor = conn.cursor()

cursor.execute(command)

cursor.close()
conn.close()