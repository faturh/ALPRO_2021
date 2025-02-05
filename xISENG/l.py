import sqlite3

DATABASE_FILE = "DBA.sqlite3"

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY,
                        item_name TEXT,
                        description TEXT,
                        damage INTEGER,
                        durability REAL
                    )""")
    conn.commit()
    conn.close()
    print("Table berhasil dibuat!")

def drop_table():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS items")
    conn.commit()
    conn.close()
    print("Table berhasil dihapus!")

def insert(id, item_name, description, damage, durability):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?)", (id, item_name, description, damage, durability))
    conn.commit()
    conn.close()
    print("Data berhasil dimasukkan!")

def select_all():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    result = c.fetchall()
    conn.close()
    for row in result:
        print(row)

def select_column(column_name):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute(f"SELECT {column_name} FROM items")
    result = c.fetchall()
    conn.close()
    for row in result:
        print(row)

def update_durability_on_id(id, durability):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("UPDATE items SET durability = ? WHERE id = ?", (durability, id))
    conn.commit()
    conn.close()
    print("Data berhasil diupdate!")

def delete_by_id(id):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print(f"Data dengan id {id} berhasil dihapus!")

def search_name(keyword):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE item_name LIKE ?", (f"%{keyword}%",))
    result = c.fetchall()
    conn.close()
    for row in result:
        print(row)

print("=====DASPRO BIZZARE ADVENTURE=====")
while True:
    print("""Pilih menu:
    1. Create table
    2. Insert data
    3. Select all
    4. Select column
    5. Update durability
    6. Delete by id
    7. Search name
    8. Drop table
    0. Exit
    """)
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