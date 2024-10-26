import sqlite3
# import os
# system = os.name
DATABASE_FILE = "DBA.sqlite3"
def create_table():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                item_name TEXT,
                description TEXT,
                damage INTEGER,
                durability REAL
            );
        """
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        cursor.close()
        conn.close()

def drop_table():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        drop_table_query = """
            DROP TABLE IF EXISTS items
        """
        cursor.execute(drop_table_query)
        conn.commit()
        print("Table berhasil di-drop!")
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        cursor.close()
        conn.close()

def insert(id, item_name, description, damage, durability):
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO items (id, item_name, description, damage, durability)
            VALUES (?, ?, ?, ?, ?)
        """
        data = (id, item_name, description, damage, durability)
        cursor.execute(insert_query, data)
        conn.commit()
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        cursor.close()
        conn.close()

def select_all():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        select_query = """ SELECT * FROM items"""
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        cursor.close()
        conn.close()

def select_column(column_name):
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        select_query = f"""
            SELECT {column_name} FROM items
        """
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        cursor.close()
        conn.close()

def update_durability_on_id(id, durability):
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute (f"UPDATE items SET durability = {durability} WHERE id = {id}") 
        conn.commit()
        print("Durability berhasil diupdate")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def delete_by_id(id):
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM items WHERE id = {id}") 
        conn.commit()
        
        print("Data berhasil dihapus")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def search_name(keyword):
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute ("""
            SELECT * FROM items WHERE item_name LIKE ?
        """, ('%'+keyword+'%',))
        rows = cursor.fetchall()
        if len(rows) > 0:
            print("Hasil search:")
            for row in rows:
                print(row)
        else:
            print("Data tidak ditemukan")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
        
print("=====DASPRO BIZZARE ADVENTURE=====")
while True:
    # match system:
    #     case "nt" : os.system("cls")
    print(
        """Pilih menu:
    1. Create table
    2. Insert data
    3. Select all
    4. Select column
    5. Update durability
    6. Delete by id
    7. Search name
    8. Drop table
    0. Exit
    """
    )
    opt = int(input())
    match opt:
        case 1:
            create_table()
            print("tabel berhasil dibuat!")
        case 2:
            id = input("Masukkan id: ")
            item_name = input("Masukkan nama item: ")
            description = input("Masukkan deskripsi item: ")
            damage = int(input("Masukkan damage item: "))
            durability = float(input("Masukkan durability item: "))
            insert(
                id=id,
                item_name=item_name,
                description=description,
                damage=damage,
                durability=durability,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            select_all()
        case 4:
            column_name = input("Masukkan nama kolom: ")
            print(f"list data pada kolom {column_name}: ")
            select_column(column_name=column_name)
        case 5:
            id = input("Masukkan id barang yang ingin diupdate: ")
            durability = input("Masukkan durability item yang baru: ")
            update_durability_on_id(id=id, durability=durability)
            print("Data berhasil diupdate!")
        case 6:
            id = int(input("Masukkan id item yang ingin dihapus: "))
            delete_by_id(id=id)
            print(f"Data dengan id {id} berhasil dihapus!")
        case 7:
            keyword = input("Masukkan keyword item yang ingin dicari: ")
            print("Hasil search: ")
            search_name(keyword=keyword)
        case 8:
            confirm = input("Apakah andas yakin? (y/n): ")
            if confirm == "y":
                drop_table()
                print("tabel berhasil di drop!")
            else:
                continue
        case 0:
            print("Program selesai dijalankan...")
            break
        case _:
            continue





import sqlite3

DATABASE_FILE = "DBA.sqlite3"

# Ubahlah semua value "pass" dari function-function dibawah dengan kode anda


def create_table():
    """Membuat table (dan database jika file belum ada)
    Args: None
    Output: Success message
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        create_table_query = """ (CREATE TABLE IF NOT EXSISTS  indifud_factory (id INTEGER PRIMARYKEY,name TEXT not null, description TEXT not null, price REAL not null)"""
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e :
        print(f"Terjadi error:{e}")
    finally:
        cursor.close()
        conn.close()



def insert(id, name, description, price):
    """Menginput data ke dalam table
    Args:
        id: int
        item_name: str
        description: str
        price: float
    Output: Success message
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        insert_query = """ INSERT INTO  indifud_factory (id,name,description,price) VALUES (?,?,?,?)"""
        data = (id,name,description,price)
        cursor.execute(insert_query,data)
        conn.commit()
    except Exception as e:
        price(f"Terjadi error{e}")
    finally:
        cursor.close()
        conn.close()

def select_all():
    
    """Print seluruh data dalam tabel
    Args: None
    Output: List data
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        select_query = """SELECT * FROM items"""
        cursor.execute(select_query)
        rows = cursor.fetchall() 
        print(rows)
    except Exception as e :
        print(f"Terjadi error {e}")
    finally:
        cursor.close()
        conn.close()


def update_description_on_id(id, description):
    """Update data description berdasarkan id dari data
    Args:
        id: int
        description: str
    Output: Success message
    Returns: None
    """
    try: 
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute (f"UPDATE  indifud_factory SET description = {description} WHERE id = {id}  ")
        conn.commit()
        print(" data berhasil di update")
    except Exception as e:
        print(f"Telah terjadi error {e}")
    finally:
        conn.close()



def delete_by_id(id):
    """Delete data berdasarkan id
    Args:
        id: int
    Output: Success message
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM indifud_factory WHERE id = {id}")
    except Exception as e:
        print(f"ERORR {e}")
    finally:
        conn.close()



def search_name(keyword):
    """Mencari data berdasarkan keyword
    Args:
        keyword: str
    Output: Data hasil search
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT * FROM indifud_factory WHERE name LIKE "{keyword}" """)
        result = cursor.fetchall()
        for row in result :
            price(row)
    except Exception as e:
        price(F"ERORR {e}")
    finally:
        conn.close()


print("=====INDIFUD=====")
while True:
    print(
        """Pilih menu:
    1. Create table
    2. Insert data
    3. Select all
    4. Update Description
    5. Delete by id
    6. Search name
    0. Exit
    """
    )

    opt = int(input())
    match opt:
        case 1:
            create_table()
            print("tabel berhasil dibuat!")
        case 2:
            id = input("Masukkan id: ")
            name = input("Masukkan nama material: ")
            description = input("Masukkan deskripsi: ")
            price = float(input("Masukkan harga: "))
            insert(
                id=id,
                name=name,
                description=description,
                price=price,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            select_all()
        case 4:
            id = input("Masukkan id barang yang ingin diupdate: ")
            durability = input("Masukkan description yang baru: ")
            update_description_on_id(id=id, description=description)
            print("Data berhasil diupdate!")
        case 5:
            id = int(input("Masukkan id item yang ingin dihapus: "))
            delete_by_id(id=id)
            print(f"Data dengan id {id} berhasil dihapus!")
        case 6:
            keyword = input("Masukkan keyword item yang ingin dicari: ")
            print("Hasil search: ")
            search_name(keyword=keyword)
        case 0:
            print("Program selesai dijalankan...")
            break
        case _:
            continue
