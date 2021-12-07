import mysql.connector as my
from mysql.connector import errorcode
import datetime

mydb = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': 'summit2'
}
x = 0
print("1 - dept")
print("2 - region")
print("3 - UPDATE")
print("9 - exit")

while x != 9:
    x = int(input("Wybierz tabelę/opcje: "))

    if x == 1:
        try:
            conn = my.connect(**mydb)
            mycursor = conn.cursor()

            myqueryd = 'SELECT d.id, d.name, r.name FROM dept d, region r WHERE r.id=d.region_id'

            mycursor.execute(myqueryd)
            print("id || name || region id ||")
            print("---++---------------++---------------------++")
            for (id, name, region_id) in mycursor:

                print("{:2d} ||{:14s} ||{:20s} ||".format(id, name, region_id))
                print("---++---------------++---------------------++")

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
    if x == 2:
        try:
            conn = my.connect(**mydb)
            mycursor = conn.cursor()

            myqueryd = 'SELECT name FROM region'

            mycursor.execute(myqueryd)

            for (name) in mycursor:
                print("|| {} ||".format(name))

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

    if x == 3:

        print("UWAGA ZMIANA NAZWY WYDZIAŁU")
        dnazw = input("dotychczasowa nazwa: ")
        nownazw = input("nowa nazwa: ")

        try:
            conn = my.connect(**mydb)
            mycursor = conn.cursor()

            myqueryd = "UPDATE dept SET name ='" + nownazw + "'WHERE name ='" + dnazw + "'"

            mycursor.execute(myqueryd)

            for (name) in mycursor:
                print("|| {} ||".format(name))

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

