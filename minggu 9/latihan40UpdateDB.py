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
mycursor = mydb.cursor()
sql = "UPDATE barang SET nama_Barang = 'tahuww' WHERE nama_Barang = 'nasi'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# ini buat delete data yang ada di data base
mycursor = mydb.cursor()
sql = "DELETE FROM barang WHERE id_Barang = '3'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")