import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testbed"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM MOCK_DATA")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# print(mydb)
