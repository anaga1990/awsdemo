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
    # sql="select * from emp where mgr='7698'"
    # sql = "select * from emp where job = 'SALESMAN' and sal >= 1250 and comm >= 300"
    # sql = "select * from emp where job != 'SALESMAN' and sal < 2500"
    # sql = "select * from emp where job != 'MANAGER' and sal > 2500 and (deptno = 20 OR deptno = 10)"
    # sql = "select * from EMP where sal between 2000 and 5000"
    sql = "SELECT * from emp left join dept On emp.deptno = dept.deptno"
    cursor.execute(sql)

    result = cursor.fetchall()

    for x in result:
        print(x)
except:
    db_conn.rollback()
db_conn.close()
