import mysql.connector as my
from mysql.connector import errorcode
mydb = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': 'summit2'
}
try:
    conn = my.connect(**mydb)
    mycursor = conn.cursor()

    myqueryd = 'SELECT name FROM dept WHERE id >= %s and id <= %s'
    myquerye = 'SELECT first_name, last_name FROM emp WHERE dept_id >= %s and dept_id <= %s'

    wybor = int(input("Wybierz departament od "))
    wybor2 = int(input("Wybierz departament do "))

    print("wybrane departamenty to: ")

    mycursor.execute(myqueryd, (wybor, wybor2))
    myresult = mycursor.fetchall()

    for i in myresult:
        print(i)

    mycursor.execute(myquerye, (wybor, wybor2))
    myresult = mycursor.fetchall()
    print("----------------------")
    print("PRACOWNICY:")
    for i in myresult:
        print(i)

except my.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("brak uprawnień")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("baza danych nie isnieje")
    else:
        print(err)

else:
    mycursor.close()
    conn.close()
