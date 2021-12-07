import mysql.connector as my
from mysql.connector import errorcode

x = input("wpisz literę nazwiska: ")

mydb = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': '39278'
}
try:
    conn = my.connect(**mydb)
    mycursor = conn.cursor()

    myqueryd = 'SELECT imie, nazwisko FROM trenerzy WHERE nazwisko LIKE ' + '"' + x + '%"'

    mycursor.execute(myqueryd)

    for (imie, nazwisko) in mycursor:

        print("{},{}".format(imie, nazwisko))

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