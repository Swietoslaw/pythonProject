import mysql.connector as my
from mysql.connector import errorcode
import datetime

mydb = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': 'summit2'
}
try:
    conn = my.connect(**mydb)
    cursor = conn.cursor()
    query = ("SELECT first_name, last_name, start_date FROM emp WHERE start_date BETWEEN %s AND %s")
    hire_start = datetime.date(1990, 1, 1)
    hire_end = datetime.date(1990, 12, 31)

    cursor.execute(query, (hire_start, hire_end))

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

except my.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("brak uprawnień")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("baza danych nie isnieje")
    else:
        print(err)

else:
    cursor.close()
    conn.close()
