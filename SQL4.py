import mysql.connector as my
from mysql.connector import errorcode

mydb = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': 'summit2'
}

def baza(y):
    try:
        conn = my.connect(**mydb)
        mycursor = conn.cursor()

        myqueryd = "SELECT * FROM " + y

        mycursor.execute(myqueryd)
        myresult = mycursor.fetchall()

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

x = baza("dept")

