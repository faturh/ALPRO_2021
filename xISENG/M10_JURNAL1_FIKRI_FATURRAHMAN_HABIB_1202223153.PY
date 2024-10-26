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
        create_table_query = """ CREATE TABLE IF NOT EXISTS database_dagangan (id INTEGER PRIMARYKEY,nama_barang TEXT not null, jumlah_barang INTEGER not null, harga_barang REAL not null)"""
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e :
        print(f"Terjadi error:{e}")
    finally:
        cursor.close()
        conn.close()



def insert(id,nama_barang,jumlah_barang,harga_barang):
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

        insert_query = """ INSERT INTO  database_dagangan (id,nama_barang,jumlah_barang,harga_barang) VALUES (?,?,?,?)"""
        data = (id,nama_barang,jumlah_barang,harga_barang)
        cursor.execute(insert_query,data)
        conn.commit()
    except Exception as e:
        print(f"Terjadi error{e}")
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

        select_query = """SELECT * FROM database_dagangan"""
        cursor.execute(select_query)
        rows = cursor.fetchall() 
        print(rows)
    except Exception as e :
        print(f"Terjadi error {e}")
    finally:
        cursor.close()
        conn.close()


def update_barang_on_id(id, jumlah_barang):
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
        cursor.execute (f"UPDATE  database_dagangan SET jumlah_barang = {jumlah_barang} WHERE id = {id}  ")
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
        cursor.execute(f"DELETE FROM database_dagangan WHERE id = {id}")
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
        cursor.execute(f"""SELECT * FROM database_dagangan WHERE nama_barang LIKE "{keyword}" """)
        result = cursor.fetchall()
        for row in result :
            print(row)
    except Exception as e:
        print(F"ERORR {e}")
    finally:
        conn.close()


print("=====WARUNG=====")
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
            id = int(input("Masukkan id: "))
            nama_barang = input("Masukkan nama barang: ")
            jumlah_barang = input("Masukkan jumlah barang: ")
            harga_barang = float(input("Masukkan harga barang: "))
            insert(
                id=id,
                nama_barang=nama_barang,
                jumlah_barang=jumlah_barang,
                harga_barang=harga_barang,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            select_all()
        case 4:
            id = input("Masukkan id barang yang ingin diupdate: ")
            durability = input("Masukkan jumlah_barang yang baru: ")
            update_barang_on_id(id=id, jumlah_barang=jumlah_barang)
            print("Data berhasil diupdate!")
        case 5:
            id = int(input("Masukkan id item yang ingin dihapus: "))
            delete_by_id(id=id)
            print(f"Data dengan id {id} berhasil dihapus!")
        case 6:
            keyword = input("Masukkan nama item yang ingin dicari: ")
            print("Hasil search: ")
            search_name(keyword=keyword)
        case 0:
            print("Program selesai dijalankan...")
            break
        case _:
            continue
