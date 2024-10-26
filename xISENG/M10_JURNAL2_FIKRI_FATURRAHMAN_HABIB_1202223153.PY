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
        create_table_query = """ CREATE TABLE IF NOT EXISTS database_dagangan (nim INTEGER PRIMARYKEY,nama_mahasiswa TEXT not null, nilai_alpro REAL not null, kelas TEXT not null)"""
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e :
        print(f"Terjadi error:{e}")
    finally:
        cursor.close()
        conn.close()



def insert(nim,nama_mahasiswa,nilai_alpro,kelas):
    """Menginput data ke dalam table
    Args:
        nim: int
        item_name: str
        description: str
        price: float
    Output: Success message
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        insert_query = """ INSERT INTO  database_dagangan (nim,name,description,price) VALUES (?,?,?,?)"""
        data = (nim,nama_mahasiswa,nilai_alpro,kelas)
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


def update_barang_on_nim(nim, nilai_alpro):
    """Update data description berdasarkan nim dari data
    Args:
        nim: int
        description: str
    Output: Success message
    Returns: None
    """
    try: 
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute (f"UPDATE  database_dagangan SET nilai_alpro = {nilai_alpro} WHERE nim = {nim}  ")
        conn.commit()
        print(" data berhasil di update")
    except Exception as e:
        print(f"Telah terjadi error {e}")
    finally:
        conn.close()



def delete_by_nim(nim):
    """Delete data berdasarkan nim
    Args:
        nim: int
    Output: Success message
    Returns: None
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM database_dagangan WHERE nim = {nim}")
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
        cursor.execute(f"""SELECT * FROM database_dagangan WHERE nama_mahasiswa LIKE "{keyword}" """)
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
    5. Delete by nim
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
            nim = int(input("Masukkan nim: "))
            nama_mahasiswa = input("Masukkan nama mahasiswa: ")
            nilai_alpro = input("Masukkan nilai alpro: ")
            kelas = input("Masukkan kelas: ")
            insert(
                nim=nim,
                nama_mahasiswa=nama_mahasiswa,
                nilai_alpro=nilai_alpro,
                kelas=kelas,
            )
            print("Data berhasil dimasukkan!")
        case 3:
            print("List item: ")
            select_all()
        case 4:
            nim = input("Masukkan nim yang ingin diupdate: ")
            durability = input("Masukkan nilai_alpro yang baru: ")
            update_barang_on_nim(nim=nim, nilai_alpro=nilai_alpro)
            print("Data berhasil diupdate!")
        case 5:
            nim = int(input("Masukkan nim yang ingin dihapus: "))
            delete_by_nim(nim=nim)
            print(f"Data dengan nim {nim} berhasil dihapus!")
        case 6:
            keyword = input("Masukkan nama yang ingin dicari: ")
            print("Hasil search: ")
            search_name(keyword=keyword)
        case 0:
            print("Program selesai dijalankan...")
            break
        case _:
            continue
