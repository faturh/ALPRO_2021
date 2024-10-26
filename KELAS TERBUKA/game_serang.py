class Hero:
          def __init__(self,name,health,attack,armor,senjata):
                    self.name = name
                    self.health = health
                    self.attack = attack
                    self.armor = armor
                    self.senjata = senjata

          def serang(self,lawan):
                    print(f'{self.name} menyerang {lawan.name}')
                    lawan.diserang (self,self.attack)

          def diserang(self,lawan,attackLawan):
                    print(f'{self.name} diserang {lawan.name}')
                    attack_diterima = (attackLawan)/self.armor
                    print (f'{self.name} akan menerima serangan sebesar {str(attack_diterima)}')
                    self.health -= attack_diterima
                    print(f'darah {self.name} tersisa : {self.health}')
          def attack_up(self,lawan,senjata):
                    self.senjata += senjata
                    attack_nambah = senjata + self.attack
                    print(f'{self.name} mendapatkan senjata bonus {senjata}')
                    print(f'{self.name} mendapatkan senjata maka menambah attack sebesar {str(senjata)}')
                    lawan.serang(self)
                    self.attack = attack_nambah


sniper = Hero('sniper', 100, 100, 10, 100)
rikimaru = Hero('rikimaru', 100, 50, 10, 0)
sniper.serang(rikimaru)
print()
rikimaru.serang(sniper)
print()
sniper.attack_up(rikimaru, 50)
print()