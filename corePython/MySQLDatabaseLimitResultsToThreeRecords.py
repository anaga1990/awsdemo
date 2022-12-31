import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root12",
    database="testmydb",
    port="3306"
)

cursor = db_conn.cursor()
try:
    cursor.execute("select * from emp limit 3")

    result = cursor.fetchall()

    for x in result:
        print(x)
except:
    db_conn.rollback()
db_conn.close()
