import mysql.connector as my

mydb = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': ''
}

conn = my.connect(**mydb)
mycursor = conn.cursor()

myqueryd = 'SELECT DISTINCT imie, nazwisko FROM zdobywca'

mycursor.execute(myqueryd)

for (imie, nazwisko) in mycursor:
    print("{},{}".format(imie, nazwisko))

else:
    mycursor.close()
    conn.close()
