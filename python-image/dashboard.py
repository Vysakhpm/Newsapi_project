import psycopg2

connection = psycopg2.connect(
    host="db-postgres-vysakh.c9moosayk8r5.ap-south-1.rds.amazonaws.com",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgresroot"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM news ;")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
