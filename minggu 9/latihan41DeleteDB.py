import mysql.connector

mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="warung putuu",
       port = "3308"
    )
# ini buat munculin data yang ada di database nya
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM barang")
myresult = mycursor.fetchall()
for x in myresult:
       print(x)
       # ini buat munculin data yang ada di database nya
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM barang")
myresult = mycursor.fetchall()
for x in myresult:
       print(x)
       if x =="":
        print("data anda kosong")
