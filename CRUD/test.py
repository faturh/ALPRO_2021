import sqlite3
import os
import CRUD as CRUD
sistem = os.name
DATABASE_FILE = "DBA.sqlite3"
def create_table():
    """Membuat table (dan database jika file belum ada)
    Args: None
    Output: Success message
    Returns: None
    """
    pass
def drop_table():
    """Mendrop table dan menghapus seluruh data yang ada didalamnya
    Args: None
    Output: Success message
    Returns: None
    """
    pass
def insert(id, item_name, description, damage, durability):
    """Memasukkan data kedalam tabel 
    Args:
        id: int
        item_name: str
        description: str
        damage: int
        durability: float
    Output: Success message
    Returns: None
    """
    pass
def select_all():
    """Print seluruh data dalam tabel
    Args: None
    Output: List data
    Returns: None
    """
    pass
def select_column(column_name):
    """Print seluruh data pada kolom tertentu
    Args:
        column_name: str
    Output: List data
    Returns: None
    """
    pass
def update_durability_on_id(id, durability):
    """Update data durability berdasarkan id dari data
    Args:
        id: int
        durability: float
    Output: Success message
    Returns: None
    """
    pass
def delete_by_id(id):
    """Menghapus data berdasarkan id
    Args:
        id: int
    Output: Success message
    Returns: None
    """
    pass
def search_name(keyword):
    """Mencari data berdasarkan keyword
    Args:
        keyword: str
    Output: Data hasil search
    Returns: None
    """
    pass
print("=====DASPRO BIZZARE ADVENTURE=====")
while True:
    match sistem:
        case "nt" : os.system("cls")
    CRUD.init_console()
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
            confirm = input("Apakah anda yakin? (y/n): ")
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