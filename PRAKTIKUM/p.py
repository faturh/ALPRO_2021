class anggota ():
    nama = "nama"
fatur = anggota()
rahman = anggota()

fatur.nama = "fatur"
rahman.nama = "rahmann"
print (fatur.nama)
print(rahman.nama)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Fatur",20)

print (f"nama anda adalah {p2.name}, anda berumur {p2.age} sekarang")


print(p1.name)
print(p1.age)