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

# ini buat insert data ke database
mycursor = mydb.cursor()
sql = "INSERT INTO barang (id_Barang,Nama_Barang,Harga_Barang) VALUES (%s,%s,%s)"
values = (3,"nasi", "5000")
mycursor.execute(sql, values)
mydb.commit()

print(mycursor.rowcount, "record inserted.")