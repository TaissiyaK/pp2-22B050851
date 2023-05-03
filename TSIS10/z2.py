import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="12345")

command = """COPY phonebook (first_name, last_name, phone_number)
            FROM 'C:\persons.csv' DELIMITER ',' CSV HEADER;"""

conn.autocommit = True
cursor = conn.cursor()

cursor.execute(command)

cursor.close()
conn.close()
