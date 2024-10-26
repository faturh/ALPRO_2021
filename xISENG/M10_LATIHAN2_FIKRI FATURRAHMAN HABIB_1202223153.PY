
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
        create_table_query = """ (CREATE TABLE IF NOT EXISTS database_toko (id INTEGER PRIMARYKEY,name TEXT not null,price REAL not null, quantity INTEGER not null, description REAL not null)"""
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e :
        print(f"Terjadi error:{e}")
    finally:
        cursor.close()
        conn.close()


def insert(id, name,price,quantity, description):
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

        insert_query = """ INSERT INTO database_toko (id, name,price,quantity, description) VALUES (?,?,?,?,?)"""
        data = (id, name,price,quantity, description)
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

        select_query = """SELECT * FROM database_toko"""
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
        cursor.execute (f"UPDATE  database_toko SET description = {description} WHERE id = {id}  ")
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
        cursor.execute(f"DELETE FROM database_toko WHERE id = {id}")
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
        cursor.execute(f"""SELECT * FROM database_toko WHERE name LIKE "{keyword}" """)
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
