import mysql.connector
import os

os.system("cls")

mydb = mysql.connector.connect(
  host      = "localhost",
  user      = "root",
  password  = "",
  database  = "warung putu",
  port      = "3308"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM barang")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM supplier")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)  