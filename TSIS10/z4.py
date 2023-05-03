import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="12345")

command = '''UPDATE phonebook SET first_name = 'Tanya' 
            WHERE phone_number = '87019933323' '''

conn.autocommit = True

cursor = conn.cursor()

cursor.execute(command)

cursor.close()
conn.close()